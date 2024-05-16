"""
Base class for real-time object detection using a Convolutional Neural Network (CNN) and computer vision library.

Simple usage example:
    ```python
    cam = camera.Camera("0", "Primary Camera", width = 640, height = 640)
    cam.run()
    ```

    ```sh
    python camera.py -C 0 -T "Primary Camera" -w 640 -h 640
    ```
"""
from argparse import ArgumentParser, Namespace, BooleanOptionalAction
from collections import deque
from multiprocessing.pool import ThreadPool
from os import curdir
from os.path import abspath, join
from torch import device
from torch.cuda import is_available as is_cuda_available
from torch.backends.mps import is_available as is_mps_available
from ultralytics import YOLO
from ultralytics.engine.results import Results
from cv2.typing import MatLike
from cv2 import (VideoCapture, namedWindow, imshow, waitKey, setTrackbarMin, getNumberOfCPUs,
                 destroyAllWindows, getTrackbarPos, createTrackbar, setNumThreads, CAP_PROP_FPS,
                 CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, WINDOW_GUI_EXPANDED, WINDOW_KEEPRATIO)

class Camera:
    def __init__(self,
                 camera: str | int = 0,
                 title: str = "Custom Object Detection",
                 model: str = join(abspath(curdir), "weights", "custom_yolov8n.pt"),
                 device: str = "cuda" if is_cuda_available() else "mps" if is_mps_available() else "cpu",
                 confidence: int = 50,
                 iou: int = 25,
                 max_detections: int = 100,
                 video_strides: int = 1,
                 width: int = 256,
                 height: int = 256,
                 fps: float = 30.0,
                 n_threads: int = 0,
                 buffer: bool = True):
        """
        Base class for real-time object detection using a Convolutional Neural Network (CNN) and computer vision library.

        Args:
            camera (str): Camera used for input. Must be streaming server `URL` for ESP32-CAM, `0` for primary camera, or `1` for secondary camera. Defaults to 0.
            title (str, optional): Window title. Defaults to "Custom Object Detection".
            model (str, optional): Detection model's path. Defaults to a model in `weights` directory.
            device (str, optional): Device running detection model. Options include: `cpu`, `cuda`, and `mps`. Defaults to available option.
            confidence (int, optional): Detection model's minimum confidence threshold. Defaults to 50.
            iou (int, optional): Lower values result in fewer detections by eliminating overlapping boxes (useful for reducing duplicates). Defaults to 25.
            max_detections (int, optional): Limits how much the model can detect in a single frame (prevents excessive outputs in dense scenes). Defaults to 100.
            video_strides (int, optional): Skip frames to speed up processing (at the cost of temporal resolution). Value of 1 processes every frame, higher values skip frames. Defaults to 1.
            width (int, optional): Camera width. Defaults to 256.
            height (int, optional): Camera height. Defaults to 256.
            fps (float, optional): Camera FPS. Defaults to 30.0.
            n_threads (int, optional): Number of threads for multithreaded video processing. If set to 0, multithreaded video processing is disabled. Defaults to 0.
            buffer (bool, optional): Determines if all frames should be buffered when processing video streams, or if the model should return the most recent frame. Defaults to True.
        """
        self._parser: ArgumentParser = ArgumentParser(description = "Run object detection model via command line", add_help = False)
        self._init_parser(camera, device, title, model, confidence, iou, max_detections, video_strides, width, height, fps, n_threads, buffer)
        self._args: Namespace = self._parser.parse_args()
        
        self._camera: VideoCapture = VideoCapture(int(self._args.cam) if self._args.cam.isdigit() else self._args.cam)
        self.confidence: int = self._args.conf
        self.iou: int = self._args.iou
        self.max_detections: int = self._args.max

        # TODO Diff vars for Windows dims / camera resolution / resolution of img passed to model
        self._camera.set(CAP_PROP_FRAME_WIDTH, self._args.width)
        self._camera.set(CAP_PROP_FRAME_HEIGHT, self._args.height)
        self._camera.set(CAP_PROP_FPS, self._args.fps)

        if self._args.n_threads > 0:
            setNumThreads(self._args.n_threads)
            self._pool: ThreadPool = ThreadPool(self._args.n_threads)
            self._pending: deque = deque()

        else:
            self._model: YOLO = YOLO(self._args.path, task = "detect")

    def _init_parser(self,
                    cam: str | int,
                    device: str,
                    title: str,
                    model: str,
                    conf: int,
                    iou: int,
                    max: int,
                    strides: int,
                    width: int,
                    height: int,
                    fps: float,
                    n_threads: int,
                    buffer: bool) -> None:
        """
        Helper method to initialize command line argument parser.

        Args:
            cam (str | int): Camera used for input.
            device (str): Device running detection model.
            title (str): Window title.
            model (str): Detection model's path.
            conf (int): Detection model's minimum confidence threshold.
            iou (int): Lower values result in fewer detections by eliminating overlapping boxes.
            detects (int): Limits how much the model can detect in a single frame.
            strides (int): Skip frames to speed up processing.
            width (int): Camera width.
            height (int): Camera height.
            fps (float): Camera FPS.
            n_threads (int): Number of threads for video processing.
            buffer (bool): Toggle stream buffering.
        """
        self._parser.add_argument("-H, --help",
                                  action = "help",
                                  help = "show this help message and exit")

        self._parser.add_argument("-C, --cam",
                                  default = cam,
                                  dest = "cam",
                                  metavar = "<camera>",
                                  help = f"set to livestream `URL` for ESP32-CAM, `0` for primary camera, or `1` for secondary camera (default: {cam})")

        self._parser.add_argument("-T, --title",
                                  type = str,
                                  default = title,
                                  dest = "title",
                                  metavar = "<title>",
                                  help = f"window title (default: \"{title}\")")

        self._parser.add_argument("-p, --path",
                                  type = str,
                                  default = model,
                                  dest = "path",
                                  metavar = "<path>",
                                  help = f"detection model's path (default: {model})")

        self._parser.add_argument("-c, --conf",
                                  type = int,
                                  default = conf,
                                  dest = "conf",
                                  metavar = "<confidence>",
                                  choices = range(1, 101),
                                  help = f"detection model's minimum confidence threshold (default: {conf})")

        self._parser.add_argument("-d, --device",
                                  type = str,
                                  default = device,
                                  dest = "device",
                                  metavar = "<device>",
                                  choices = [ "cuda", "mps", "cpu" ],
                                  help = f"device running detection model (default: {device})")

        self._parser.add_argument("-i, --iou",
                                  type = int,
                                  default = iou,
                                  dest = "iou",
                                  metavar = "<iou>",
                                  choices = range(1, 101),
                                  help = f"lower values eliminate overlapping boxes (default: {iou})")

        self._parser.add_argument("-m, --max",
                                  type = int,
                                  default = max,
                                  dest = "max",
                                  metavar = "<max-detections>",
                                  help = f"limit number of detections per frame (default: {max})")

        self._parser.add_argument("-s, --strides",
                                  type = int,
                                  default = strides,
                                  dest = "strides",
                                  metavar = "<strides>",
                                  help = f"1 processes every frame, higher values skip frames (default: {strides})")

        self._parser.add_argument("-w, --width",
                                  type = int,
                                  default = width,
                                  dest = "width",
                                  metavar = "<width>",
                                  help = f"camera width (default: {width})")

        self._parser.add_argument("-h, --height",
                                  type = int,
                                  default = height,
                                  dest = "height",
                                  metavar = "<height>",
                                  help = f"camera height (default: {height})")

        self._parser.add_argument("-f, --fps",
                                  type = float,
                                  default = fps,
                                  dest = "fps",
                                  metavar = "<fps>",
                                  help = f"camera frames per second (default: {fps})")

        self._parser.add_argument("-n, --n-threads",
                                  type = int,
                                  default = n_threads,
                                  dest = "n_threads",
                                  metavar = "<threads>",
                                  choices = range(1, getNumberOfCPUs() + 1),
                                  help = f"number of video processing threads; if set to 0, multithreaded video processing is disabled (default: {n_threads})")

        self._parser.add_argument("-b, --buffer",
                                  action = BooleanOptionalAction,
                                  type = bool,
                                  default = buffer,
                                  dest = "buffer",
                                  help = f"toggle livestream buffering (default: {buffer})")

    def run(self) -> None:
        """
        Run detection model.
        """                
        while self._camera.isOpened():
            # Fetch camera frame
            success, frame = self._camera.read()

            if success:
                # If multithreaded video processing is enabled
                if self._args.n_threads > 0:
                    # Process pending tasks
                    while len(self._pending) > 0 and self._pending[0].ready():
                        # Get model's inference result(s)
                        result = self._pending.popleft().get()

                        # Show livestream with bounding boxes over detections
                        self._show_window(result)

                    # Start new task if there are less than `self._args.n_threads` tasks pending
                    if len(self._pending) < self._args.n_threads:
                        # Process asynchronously
                        task = self._pool.apply_async(self._process_frame, (frame,))

                        # Add to deque
                        self._pending.append(task)

                else:                    
                    # Run detection model on the frame
                    result = self._process_frame(frame)

                    # Show livestream with bounding boxes over detections
                    self._show_window(result)

            # End program when "Escape" is pressed
            self._quit()

    def _process_frame(self, frame: MatLike) -> list[Results]:
        """
        Run inference on frame with detection model.

        Args:
            frame (MatLike): Camera frame.

        Returns:
            list[Results]: Detection model's prediction(s).
        """
        # Ensures it's thread-safe
        local_model = YOLO(self._args.path, task = "detect") if self._args.n_threads > 0 else self._model
        
        return local_model(frame,
                           stream = True,
                           device = device(self._args.device),
                           stream_buffer = self._args.buffer,
                           vid_stride = self._args.strides,
                           conf = self.confidence / 100.0,
                           iou = self.iou / 100.0,
                           max_det = self.max_detections,
                           imgsz = (self._args.height, self._args.width),
                           agnostic_nms = True)

    def _quit(self) -> None:
        """
        When `Escape` is pressed:
        
        1. Close camera
        2. Close window
        3. Exit program
        """
        if waitKey(1) & 0xFF == 27:
            self._camera.release()
            destroyAllWindows() 
            exit(0)
            
    def _update_confidence(self, new_conf: int) -> None:
        """
        Callback function for confidence trackbar.

        Args:
            new_conf (int): New confidence value.
        """
        self.confidence = new_conf

    def _update_iou(self, new_iou: int) -> None:
        """
        Callback function for IoU trackbar.

        Args:
            new_iou (int): New IoU value.
        """
        self.iou = new_iou
        
    def _update_max_detections(self, new_max: int) -> None:
        """
        Callback function for max detections trackbar.

        Args:
            new_max (int): New max detections value.
        """
        self.max_detections = new_max

    def _show_window(self, results: list[Results]) -> None:
        """
        Show livestream with bounding boxes over detections.

        Args:
            results (list[Results]): Inference results.
        """
        # Create resizable, named window
        namedWindow(self._args.title, WINDOW_GUI_EXPANDED | WINDOW_KEEPRATIO)

        # Create trackbars for confidence, IOU, and maximum detections
        createTrackbar("Confidence", self._args.title, self.confidence, 100, self._update_confidence)
        createTrackbar("IoU", self._args.title, self.iou, 100, self._update_iou)
        createTrackbar("Max Detects", self._args.title, self.max_detections, self._args.max, self._update_max_detections)

        # Ensure confidence and IOU are at least 1% so program doesn't hang/freeze
        setTrackbarMin("Confidence", self._args.title, 1)
        setTrackbarMin("IoU", self._args.title, 1)
        
        for result in results:
            # Update trackbars for confidence, IOU, and maximum detections
            getTrackbarPos("Confidence", self._args.title)
            getTrackbarPos("IoU", self._args.title)
            getTrackbarPos("Max Detects", self._args.title)
            
            # Annotate the frame with its result, then show in window
            imshow(self._args.title, result.plot())

if __name__ == "__main__":
    # Start detection program
    Camera().run()