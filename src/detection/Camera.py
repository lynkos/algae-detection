from argparse import ArgumentParser, Namespace
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
                 CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS, WINDOW_GUI_EXPANDED)

class Camera:
    def __init__(self,
                 camera_type: str | None = None,
                 title: str = "Algae Detector",
                 model_name: str = "custom_yolov8x_v2.pt",
                 device_type: str = "mps" if is_mps_available() else "cuda" if is_cuda_available() else "cpu",
                 confidence: float = 0.25,
                 iou: float = 0.5,
                 max_detections: int = 100,
                 video_strides: int = 5,
                 width: int = 640,
                 height: int = 640,
                 fps: float = 30.0,
                 n_threads: int = getNumberOfCPUs()):
        """
        Base class for camera object detection.

        Args:
            camera_type (str | None): Camera used for input. Set to streaming server's URL for ESP32-CAM, "0" for Webcam, "1" for iPhone.
            title (str, optional): Window title. Defaults to "Algae Detector".
            model_name (str, optional): Detection model's name. Defaults to a model in `weights`.
            device_type (str, optional): Device to run detection model on. Options include: "cuda", "mps", and "cpu". Defaults to whichever option is available.
            confidence (float, optional): Detection model's minimum confidence threshold. Defaults to 0.25.
            iou (float, optional): Lower values result in fewer detections by eliminating overlapping boxes (useful for reducing duplicates). Defaults to 0.5.
            max_detections (int, optional): Limits how much the model can detect in a single frame (prevents excessive outputs in dense scenes). Defaults to 100.
            video_strides (int, optional): Allows skipping frames in stream to speed up processing (at the cost of temporal resolution). 1 processes every frame, higher values skip frames. Defaults to 5.
            width (int, optional): Camera width. Defaults to 640.
            height (int, optional): Camera height. Defaults to 640.
            fps (float, optional): Camera FPS. Defaults to 30.0.
            n_threads (int, optional): Number of threads for video processing. Defaults to number of logical CPUs available.
        """
        self._parser: ArgumentParser = ArgumentParser(description = "Command line parser for object detection.")
        self._init_parser(camera_type, device_type, title, model_name, confidence, iou, max_detections, video_strides, width, height, fps, n_threads)
        self._args: Namespace = self._parser.parse_args()
        
        self._camera: VideoCapture = VideoCapture(int(self._args.camera) if self._args.camera is not None and self._args.camera.isdigit() else self._args.camera)
        self._yolo_model: YOLO = YOLO(join(abspath(curdir), "weights", self._args.name), task = "detect")
        self.confidence: float = self._args.conf
        self.iou: float = self._args.iou
        self.max_detections: int = self._args.max
        
        self._camera.set(CAP_PROP_FRAME_WIDTH, self._args.width)
        self._camera.set(CAP_PROP_FRAME_HEIGHT, self._args.height)
        self._camera.set(CAP_PROP_FPS, self._args.fps)
        
        setNumThreads(self._args.threads)
        self._pool: ThreadPool = ThreadPool(self._args.threads)
        self._pending: deque = deque()

    def _init_parser(self,
                    camera_type: str | None,
                    device: str,
                    title: str,
                    model: str,
                    confidence: float,
                    iou: float,
                    max_detects: int,
                    strides: int,
                    width: int,
                    height: int,
                    fps: float,
                    n_threads: int) -> None:
        """
        Helper method to initialize command line parser.

        Args:
            camera_type (str | None): Camera used for input. If None (i.e., hasn't been declared in instance), then it is a required command line argument.
            device (str): Device to run detection model on.
            title (str): Window title
            model_name (str): Detection model's name.
            confidence (float): Detection model's minimum confidence threshold.
            iou (float): Lower values result in fewer detections by eliminating overlapping boxes.
            max_detects (int): Limits how much the model can detect in a single frame.
            strides (int): Allows skipping frames in stream to speed up processing (at the cost of temporal resolution).
            width (int): Camera width.
            height (int): Camera height.
            fps (float): Camera FPS.
            n_threads (int): Number of threads for video processing.
        """
        self._parser.add_argument("-C", "--camera",
                                  default = camera_type,
                                  required = True if camera_type is None else False,
                                  help = "Camera used for input. Set to streaming server's URL for ESP32-CAM, 0 for Webcam, 1 for iPhone.")

        self._parser.add_argument("-T", "--title",
                                  type = str,
                                  default = title,
                                  required = False,
                                  help = f"Window title. Defaults to {title}.")

        self._parser.add_argument("-N", "--name",
                                  type = str,
                                  default = model,
                                  required = False,
                                  help = f"Detection model's name. Defaults to {model}.")

        self._parser.add_argument("-D", "--device",
                                  type = str,
                                  default = device,
                                  required = False,
                                  help = f"Device to run detection model on. Options include: 'cuda', 'mps', and 'cpu'. Defaults to {device}.")

        self._parser.add_argument("--conf", "--confidence",
                                  type = float,
                                  default = confidence,
                                  required = False,
                                  help = f"Detection model's minimum confidence threshold. Defaults to {confidence}.")

        self._parser.add_argument("-I", "--iou",
                                  type = float,
                                  default = iou,
                                  required = False,
                                  help = f"Lower values result in fewer detections by eliminating overlapping boxes (useful for reducing duplicates). Defaults to {iou}.")

        self._parser.add_argument("-M", "--max",
                                  type = int,
                                  default = max_detects,
                                  required = False,
                                  help = f"Limits how much the model can detect in a single frame (prevents excessive outputs in dense scenes). Defaults to {max_detects}.")

        self._parser.add_argument("-S", "--strides",
                                  type = int,
                                  default = strides,
                                  required = False,
                                  help = f"Skips frames in stream to speed up processing, but at the cost of temporal resolution. 1 processes every frame, higher values skip frames. Defaults to {strides}.")

        self._parser.add_argument("-W", "--width",
                                  type = int,
                                  default = width,
                                  required = False,
                                  help = f"Camera width. Defaults to {width}.")

        self._parser.add_argument("-H", "--height",
                                  type = int,
                                  default = height,
                                  required = False,
                                  help = f"Camera height. Defaults to {height}.")

        self._parser.add_argument("-F", "--fps",
                                  type = float,
                                  default = fps,
                                  required = False,
                                  help = f"Camera FPS. Defaults to {fps}.")

        self._parser.add_argument("--threads",
                                  type = int,
                                  default = n_threads,
                                  required = False,
                                  help = f"Number of threads for video processing. Defaults to {n_threads}.")

    def run(self) -> None:
        """
        Run detection model with multithreaded video processing.
        """
        while self._camera.isOpened():
            # Process pending tasks
            while len(self._pending) > 0 and self._pending[0].ready():
                # Get model's inference result(s)
                result = self._pending.popleft().get()

                # Show livestream with bounding boxes over detections
                self._showWindow(result)

            # Start new task if there are less than `self._args.threads` tasks pending
            if len(self._pending) < self._args.threads:
                # Fetch camera frame
                success, frame = self._camera.read()

                if success:
                    # Process asynchronously
                    task = self._pool.apply_async(self._process_frame, (frame,))

                    # Add to deque
                    self._pending.append(task)

            # Finish when "Escape" is pressed
            self._quit()

    def _process_frame(self, frame: MatLike) -> list[Results]:
        """
        Use detection model on frame.

        Args:
            frame (MatLike): Camera frame.

        Returns:
            list[Results]: Inference results.
        """
        return self._yolo_model(frame,
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
        When 'Escape' is pressed:
        
        1. Close camera
        2. Close window
        3. Exit program
        """
        if waitKey(1) & 0xFF == 27:
            self._camera.release()
            destroyAllWindows() 
            exit(0)
            
    def _changeConfidence(self, new_conf: int) -> None:
        """
        Callback function for confidence trackbar.

        Args:
            new_conf (int): New confidence value.
        """
        self.confidence = new_conf / 100.0

    def _changeIOU(self, new_iou: int) -> None:
        """
        Callback function for IOU trackbar.

        Args:
            new_iou (int): New IOU value.
        """
        self.iou = new_iou / 100.0
        
    def _changeMaxDetections(self, new_max_det: int) -> None:
        """
        Callback function for max detections trackbar.

        Args:
            new_max_det (int): New max detections value.
        """
        self.max_detections = new_max_det

    def _showWindow(self, results: list[Results]) -> None:
        """
        Show livestream with bounding boxes over detections.

        Args:
            results (list[Results]): Inference results.
        """
        # Create resizable, named window
        namedWindow(self._args.title, WINDOW_GUI_EXPANDED)

        # Create trackbars for confidence, IOU, and maximum detections
        createTrackbar("Confidence", self._args.title, int(self.confidence * 100), 100, self._changeConfidence)
        createTrackbar("IoU", self._args.title, int(self.iou * 100), 100, self._changeIOU)
        createTrackbar("Max Detects", self._args.title, self.max_detections, self._args.max, self._changeMaxDetections)

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
    Camera("1").run()