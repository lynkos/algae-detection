"""
Base class for real-time object detection using a fine-tuned Convolutional Neural Network (CNN) model and computer vision library OpenCV.

Simple usage example:
    ```python
    cam = camera.Camera("0", "Primary Camera", width = 640, height = 640)
    cam.run()
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
                 destroyAllWindows, getTrackbarPos, createTrackbar, setNumThreads,
                 CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS, WINDOW_KEEPRATIO)

class Camera:
    def __init__(self,
                 camera: str,
                 title: str = "Custom Object Detection",
                 model: str = join(abspath(curdir), "weights", "custom_yolov8x_v2.pt"),
                 device: str = "cuda" if is_cuda_available() else "mps" if is_mps_available() else "cpu",
                 confidence: float = 0.25,
                 iou: float = 0.5,
                 max_detections: int = 100,
                 video_strides: int = 1,
                 width: int = 640,
                 height: int = 640,
                 fps: float = 30.0,
                 threading: bool = False,
                 n_threads: int = getNumberOfCPUs()):
        """
        Base class for real-time object detection using a fine-tuned Convolutional Neural Network (CNN) model and computer vision library OpenCV.

        Args:
            camera (str): Camera used for input. Must be streaming server `URL` for ESP32-CAM, `0` for primary camera, or `1` for secondary camera.
            title (str, optional): Window title. Defaults to "Custom Object Detection".
            model (str, optional): Detection model's path. Defaults to a model in weights.
            device (str, optional): Device running detection model. Options include: `cpu`, `cuda`, and `mps`. Defaults to available option.
            confidence (float, optional): Detection model's minimum confidence threshold. Defaults to 0.25.
            iou (float, optional): Lower values result in fewer detections by eliminating overlapping boxes (useful for reducing duplicates). Defaults to 0.5.
            max_detections (int, optional): Limits how much the model can detect in a single frame (prevents excessive outputs in dense scenes). Defaults to 100.
            video_strides (int, optional): Skip frames to speed up processing (at the cost of temporal resolution). Value of 1 processes every frame, higher values skip frames. Defaults to 1.
            width (int, optional): Camera width. Defaults to 640.
            height (int, optional): Camera height. Defaults to 640.
            fps (float, optional): Camera FPS. Defaults to 30.0.
            threading (bool, optional): Whether or not to use multithreaded video processing. Defaults to False.
            n_threads (int, optional): Number of threads for video processing; only applicable when `threading = True`. Defaults to number of logical CPUs available.
        """
        self._parser: ArgumentParser = ArgumentParser(description = "Run object detection model via command line", add_help = False)
        self._init_parser(camera, device, title, model, confidence, iou, max_detections, video_strides, width, height, fps, threading, n_threads)
        self._args: Namespace = self._parser.parse_args()
        
        self._camera: VideoCapture = VideoCapture(int(self._args.cam) if self._args.cam.isdigit() else self._args.cam)
        self._model: YOLO = YOLO(self._args.path, task = "detect")
        self.confidence: float = self._args.conf
        self.iou: float = self._args.iou
        self.max_detections: int = self._args.max
        
        self._camera.set(CAP_PROP_FRAME_WIDTH, self._args.width)
        self._camera.set(CAP_PROP_FRAME_HEIGHT, self._args.height)
        self._camera.set(CAP_PROP_FPS, self._args.fps)

        if self._args.threads:
            setNumThreads(self._args.n_threads)
            self._pool: ThreadPool = ThreadPool(self._args.n_threads)
            self._pending: deque = deque()

    def _init_parser(self,
                    cam: str,
                    device: str,
                    title: str,
                    model: str,
                    conf: float,
                    iou: float,
                    max: int,
                    strides: int,
                    width: int,
                    height: int,
                    fps: float,
                    threading: bool,
                    n_threads: int) -> None:
        """
        Helper method to initialize command line argument parser.

        Args:
            cam (str): Camera used for input.
            device (str): Device running detection model.
            title (str): Window title.
            model (str): Detection model's path.
            conf (float): Detection model's minimum confidence threshold.
            iou (float): Lower values result in fewer detections by eliminating overlapping boxes.
            detects (int): Limits how much the model can detect in a single frame.
            strides (int): Skip frames to speed up processing.
            width (int): Camera width.
            height (int): Camera height.
            fps (float): Camera FPS.
            threading (bool): Toggle multithreaded video processing.
            n_threads (int): Number of threads for video processing.
        """
        self._parser.add_argument("-H, --help",
                                  action = "help",
                                  help = "show this help message and exit")

        self._parser.add_argument("-C, --cam",
                                  type = str,
                                  default = cam,
                                  dest = "cam",
                                  metavar = "<camera>",
                                  required = True if not cam else False,
                                  help = "set to livestream `URL` for ESP32-CAM, `0` for primary camera, or `1` for secondary camera")

        self._parser.add_argument("-T, --title",
                                  type = str,
                                  default = title,
                                  dest = "title",
                                  metavar = "<title>",
                                  help = f"window title (default: {title})")

        self._parser.add_argument("-p, --path",
                                  type = str,
                                  default = model,
                                  dest = "path",
                                  metavar = "<path>",
                                  help = f"detection model's path (default: {model})")

        self._parser.add_argument("-c, --conf",
                                  type = float,
                                  default = conf,
                                  dest = "conf",
                                  metavar = "<confidence>",
                                  help = f"detection model's minimum confidence threshold (default: {conf})")

        self._parser.add_argument("-d, --device",
                                  type = str,
                                  default = device,
                                  dest = "device",
                                  metavar = "<device>",
                                  choices = [ "cuda", "mps", "cpu" ],
                                  help = f"device running detection model (default: {device})")

        self._parser.add_argument("-i, --iou",
                                  type = float,
                                  default = iou,
                                  dest = "iou",
                                  metavar = "<iou>",
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

        self._parser.add_argument("-t, --threads",
                                  action = BooleanOptionalAction,
                                  default = threading,
                                  dest = "threads",
                                  help = f"toggle multithreaded video processing (default: {threading})")

        self._parser.add_argument("-n, --n-threads",
                                  type = int,
                                  default = n_threads,
                                  dest = "n_threads",
                                  metavar = "<threads>",
                                  choices = range(1, getNumberOfCPUs() + 1),
                                  help = f"number of video processing threads (default: {n_threads})")

    def run(self) -> None:
        """
        Run detection model.
        """                
        while self._camera.isOpened():
            # Fetch camera frame
            success, frame = self._camera.read()

            if success:
                # If multithreaded video processing is enabled
                if self._args.threads:
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
        return self._model(frame,
                           stream = True,
                           device = device(self._args.device),
                           stream_buffer = True,
                           vid_stride = self._args.strides,
                           conf = self.confidence,
                           iou = self.iou,
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
            
    def _change_confidence(self, new_conf: int) -> None:
        """
        Callback function for confidence trackbar.

        Args:
            new_conf (int): New confidence value.
        """
        self.confidence = new_conf / 100.0

    def _change_iou(self, new_iou: int) -> None:
        """
        Callback function for IOU trackbar.

        Args:
            new_iou (int): New IOU value.
        """
        self.iou = new_iou / 100.0
        
    def _change_max_detections(self, new_max_det: int) -> None:
        """
        Callback function for max detections trackbar.

        Args:
            new_max_det (int): New max detections value.
        """
        self.max_detections = new_max_det

    def _show_window(self, results: list[Results]) -> None:
        """
        Show livestream with bounding boxes over detections.

        Args:
            results (list[Results]): Inference results.
        """
        # Create resizable, named window
        namedWindow(self._args.title, WINDOW_KEEPRATIO)

        # Create trackbars for confidence, IOU, and maximum detections
        createTrackbar("Confidence", self._args.title, int(self.confidence * 100), 100, self._change_confidence)
        createTrackbar("IoU", self._args.title, int(self.iou * 100), 100, self._change_iou)
        createTrackbar("Max Detects", self._args.title, self.max_detections, self._args.max, self._change_max_detections)

        # Ensure confidence and IOU are at least 1% to avoid program from hanging/freezing
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
    Camera("0").run()