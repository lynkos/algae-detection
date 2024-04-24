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

DEVICE: device = device("mps") if is_mps_available() else device("cuda") if is_cuda_available() else device("cpu")
CONFIDENCE: float = 0.25
IOU: float = 0.5
STRIDES: int = 5
MAX_DETECTIONS: int = 100
WIDTH: int = 1280
HEIGHT: int = 720
FPS: float = 30.0
"""Default algae detection attributes"""

MODEL_PATH: str = join(abspath(curdir), "weights", "custom_yolov8x_v2.pt")
"""Default path of custom-trained algae detection model"""

class Camera:
    def __init__(self,
                 camera_type: str | int,
                 title: str = "Algae Detector",
                 model_path: str = MODEL_PATH,
                 device_type: device | str = DEVICE,
                 confidence: float = CONFIDENCE,
                 iou: float = IOU,
                 max_detections: int = MAX_DETECTIONS,
                 video_strides: int = STRIDES,
                 width: int = WIDTH,
                 height: int = HEIGHT,
                 fps: float = FPS,
                 n_threads: int = getNumberOfCPUs()):
        """
        Base class for camera object detection.

        Args:
            camera_type (str | int): Camera used for input. Set to streaming server's URL for ESP32-CAM, `0` for Webcam, `1` for iPhone.
            title (str, optional): Window title. Defaults to "Algae Detector".
            model_path (str, optional): Algae detection model's path. Defaults to `MODEL_PATH`.
            device_type (device | str, optional): Device (GPU or CPU) to run algae detection model on. Defaults to `DEVICE`.
            confidence (float, optional): Algae detection model's minimum confidence threshold. Defaults to `CONFIDENCE`.
            iou (float, optional): Lower values result in fewer detections by eliminating overlapping boxes (useful for reducing duplicates). Defaults to `IOU`.
            max_detections (int, optional): Limits how many algae the model can detect in a single frame (prevents excessive outputs in dense scenes). Defaults to `MAX_DETECTIONS`.
            video_strides (int, optional): Allows skipping frames in stream to speed up processing (at the cost of temporal resolution). Value of `1` processes every frame, higher values skip frames. Defaults to `STRIDES`.
            width (int, optional): Camera width. Defaults to `WIDTH`.
            height (int, optional): Camera height. Defaults to `HEIGHT`.
            fps (float, optional): Camera FPS. Defaults to `FPS`.
            n_threads (int, optional): Number of threads for video processing. Defaults to number of logical CPUs available.
        """
        self.camera: VideoCapture = VideoCapture(camera_type)
        self.title: str = title
        self._yolo_model: YOLO = YOLO(model_path, task = "detect")
        self.confidence: float = confidence
        self.device: device | str = device_type
        self.iou: float = iou
        self.max_detections: int = max_detections
        self.max_detections_limit: int = max_detections
        self.strides: int = video_strides
        
        self.width: int = width
        self.height: int = height
        self.camera.set(CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(CAP_PROP_FRAME_HEIGHT, height)
        self.camera.set(CAP_PROP_FPS, fps)
        
        setNumThreads(n_threads)
        self._pool: ThreadPool = ThreadPool(n_threads)
        self._n_threads: int = n_threads
        self._pending: deque = deque()

    def run(self) -> None:
        """
        Run algae detection model with multithreaded video processing.
        """
        while self.camera.isOpened():
            # Process pending tasks
            while len(self._pending) > 0 and self._pending[0].ready():
                # Get model's inference result(s)
                result = self._pending.popleft().get()

                # Show livestream with bounding boxes over detected algae
                self._showWindow(result)

            # Start new task if there are less than `self._n_threads` tasks pending
            if len(self._pending) < self._n_threads:
                # Fetch camera frame
                success, frame = self.camera.read()

                if success:
                    # Process asynchronously
                    task = self._pool.apply_async(self._process_frame, (frame,))

                    # Add to deque
                    self._pending.append(task)

            # Finish when "Escape" is pressed
            self._quit()

    def _process_frame(self, frame: MatLike) -> list[Results]:
        """
        Use algae detection model on frame.

        Args:
            frame (MatLike): Camera frame.

        Returns:
            list[Results]: Inference results.
        """
        return self._yolo_model(frame,
                                stream = True,
                                device = self.device,
                                stream_buffer = True,
                                vid_stride = self.strides,
                                conf = self.confidence,
                                iou = self.iou,
                                max_det = self.max_detections,
                                imgsz = (self.height, self.width),
                                agnostic_nms = True)
    
    def _quit(self) -> None:
        """
        When 'Escape' is pressed:
        
        1. Close camera
        2. Close window
        3. Exit program
        """
        if waitKey(1) & 0xFF == 27:
            self.camera.release()
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
        Show livestream with bounding boxes over detected algae.

        Args:
            results (list[Results]): Inference results.
        """
        # Create resizable, named window
        namedWindow(self.title, WINDOW_GUI_EXPANDED)

        # Create trackbars for confidence, IOU, and maximum detections
        createTrackbar("Confidence", self.title, int(self.confidence * 100), 100, self._changeConfidence)
        createTrackbar("IoU", self.title, int(self.iou * 100), 100, self._changeIOU)
        createTrackbar("Max Detects", self.title, self.max_detections, self.max_detections_limit, self._changeMaxDetections)

        # Ensure confidence and IOU are at least 1 to prevent program from hanging/freezing
        setTrackbarMin("Confidence", self.title, 1)
        setTrackbarMin("IoU", self.title, 1)
        
        for result in results:
            # Update trackbars for confidence, IOU, and maximum detections
            getTrackbarPos("Confidence", self.title)
            getTrackbarPos("IoU", self.title)
            getTrackbarPos("Max Detects", self.title)
            
            # Annotate the frame with its result, then show in window
            imshow(self.title, result.plot())