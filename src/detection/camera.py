"""
Base class for object detection with a fine-tuned Convolutional Neural Network (CNN) model.

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
                 device: str = "mps" if is_mps_available() else "cuda" if is_cuda_available() else "cpu",
                 confidence: float = 0.25,
                 iou: float = 0.5,
                 max_detections: int = 100,
                 video_strides: int = 5,
                 width: int = 640,
                 height: int = 640,
                 fps: float = 30.0,
                 threading: bool = False,
                 n_threads: int = getNumberOfCPUs()):
        """
        Base class for object detection with a fine-tuned Convolutional Neural Network (CNN) model.

        Args:
            camera (str): Camera used for input. Set to streaming server's `URL` for ESP32-CAM, `0` for primary camera, `1` for secondary camera.
            title (str, optional): Window title. Defaults to "Custom Object Detection".
            model (str, optional): Detection model's path. Defaults to a model in weights.
            device (str, optional): Device running detection model. Options include: `cpu`, `cuda`, and `mps`. Defaults to available option.
            confidence (float, optional): Detection model's minimum confidence threshold. Defaults to 0.25.
            iou (float, optional): Lower values result in fewer detections by eliminating overlapping boxes (useful for reducing duplicates). Defaults to 0.5.
            max_detections (int, optional): Limits how much the model can detect in a single frame (prevents excessive outputs in dense scenes). Defaults to 100.
            video_strides (int, optional): Skip frames to speed up processing (at the cost of temporal resolution). Value of 1 processes every frame, higher values skip frames. Defaults to 5.
            width (int, optional): Camera width. Defaults to 640.
            height (int, optional): Camera height. Defaults to 640.
            fps (float, optional): Camera FPS. Defaults to 30.0.
            threading (bool, optional): Whether or not to use multithreaded video processing. Defaults to False.
            n_threads (int, optional): Number of threads for video processing. Defaults to number of logical CPUs available.
        """
        self._parser: ArgumentParser = ArgumentParser(description = "Command line parser for `camera.py`")
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
        self._parser.add_argument("-C, --cam",
                                  type = str,
                                  default = cam,
                                  dest = "cam",
                                  metavar = "<camera>",
                                  help = "Camera used for input. Set to streaming server's `URL` for ESP32-CAM, `0` for primary camera, `1` for secondary camera.")

        self._parser.add_argument("-t, --title",
                                  type = str,
                                  default = title,
                                  dest = "title",
                                  metavar = "<window-title>",
                                  help = f"Window title. Defaults to {title}.")

        self._parser.add_argument("-p, --path",
                                  type = str,
                                  default = model,
                                  dest = "path",
                                  metavar = "<model-path>",
                                  help = f"Detection model's path. Defaults to {model}.")

        self._parser.add_argument("-d, --device",
                                  type = str,
                                  default = device,
                                  dest = "device",
                                  metavar = "<device>",
                                  help = f"Device running detection model. Options include: `cuda`, `mps`, and `cpu`. Defaults to {device}.")

        self._parser.add_argument("-c, --conf",
                                  type = float,
                                  default = conf,
                                  dest = "conf",
                                  metavar = "<confidence>",
                                  help = f"Detection model's minimum confidence threshold. Defaults to {conf}.")

        self._parser.add_argument("-i, --iou",
                                  type = float,
                                  default = iou,
                                  dest = "iou",
                                  metavar = "<iou>",
                                  help = f"Lower values result in fewer detections by eliminating overlapping boxes (useful for reducing duplicates). Defaults to {iou}.")

        self._parser.add_argument("-m, --max",
                                  type = int,
                                  default = max,
                                  dest = "max",
                                  metavar = "<max-detections>",
                                  help = f"Limits how much the model can detect in a single frame (prevents excessive outputs in dense scenes). Defaults to {max}.")

        self._parser.add_argument("-s, --strides",
                                  type = int,
                                  default = strides,
                                  dest = "strides",
                                  metavar = "<video-strides>",
                                  help = f"Skips frames in stream to speed up processing (at the cost of temporal resolution). `1` processes every frame, higher values skip frames. Defaults to {strides}.")

        self._parser.add_argument("-w, --width",
                                  type = int,
                                  default = width,
                                  dest = "width",
                                  metavar = "<width>",
                                  help = f"Camera width. Defaults to {width}.")

        self._parser.add_argument("-h, --height",
                                  type = int,
                                  default = height,
                                  dest = "height",
                                  metavar = "<height>",
                                  help = f"Camera height. Defaults to {height}.")

        self._parser.add_argument("-f, --fps",
                                  type = float,
                                  default = fps,
                                  dest = "fps",
                                  metavar = "<fps>",
                                  help = f"Camera FPS. Defaults to {fps}.")

        self._parser.add_argument("-T, --threads",
                                  action = BooleanOptionalAction,
                                  default = threading,
                                  dest = "threads",
                                  help = f"Whether or not to use multithreaded video processing. Defaults to {threading}.")

        self._parser.add_argument("-n, --n-threads",
                                  type = int,
                                  default = n_threads,
                                  dest = "n_threads",
                                  metavar = "<threads>",
                                  choices = range(1, getNumberOfCPUs() + 1),
                                  help = f"Number of threads for video processing. Defaults to {n_threads}.")

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
        Use detection model on frame.

        Args:
            frame (MatLike): Camera frame.

        Returns:
            list[Results]: Inference results.
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