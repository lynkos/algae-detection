from torch import device
from torch.cuda import is_available as is_cuda_available
from torch.backends.mps import is_available as is_mps_available
from ultralytics import YOLO
from os import curdir
from os.path import abspath, join
from cv2 import (VideoCapture, namedWindow, imshow, waitKey, setTrackbarMin, 
                 destroyAllWindows, getTrackbarPos, createTrackbar, WINDOW_GUI_EXPANDED,
                 CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS)

DEVICE: device = device("mps") if is_mps_available() else device("cuda") if is_cuda_available() else device("cpu")
CONFIDENCE: float = 0.25
IOU: float = 0.5
STRIDES: int = 5
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
                 video_strides: int = STRIDES,
                 width: int = WIDTH,
                 height: int = HEIGHT,
                 fps: float = FPS):
        """
        Base class for camera object detection.

        Args:
            camera_type (str | int): Which camera to use. Set to streaming URL for ESP32-CAM, `0` for Webcam, `1` for iPhone.
            title (str, optional): Window title. Defaults to "Algae Detector".
            model_path (str, optional): Detection model's path. Defaults to `MODEL_PATH`.
            device_type (device | str, optional): Device (GPU or CPU) to run detection model on. Defaults to `DEVICE`.
            confidence (float, optional): Detection model's confidence threshold. Defaults to `CONFIDENCE`.
            iou (float, optional): Lower values result in fewer detections by eliminating overlapping boxes, useful for reducing duplicates. Defaults to `IOU`.
            video_strides (int, optional): Allows skipping frames in videos to speed up processing at the cost of temporal resolution. Value of `1` processes every frame, higher values skip frames. Defaults to `STRIDES`.
            width (int, optional): Camera width. Defaults to `WIDTH`.
            height (int, optional): Camera height. Defaults to `HEIGHT`.
            fps (float, optional): Camera FPS. Defaults to `FPS`.
        """
        self.camera: VideoCapture = VideoCapture(camera_type)
        self.title: str = title
        self._yolo_model: YOLO = YOLO(model_path, task = "detect")
        self.confidence: float = confidence
        self.device: device | str = device_type
        self.iou: float = iou
        self.strides: int = video_strides
        self.width: int = width
        self.height: int = height
        self.camera.set(CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(CAP_PROP_FRAME_HEIGHT, height)
        self.camera.set(CAP_PROP_FPS, fps)

    def run(self) -> None:
        """
        Run camera object detection.
        """
        while self.camera.isOpened():
            # Fetch camera frame
            success, frame = self.camera.read()

            if success:
                # Run algae detection model on the frame
                results = self._yolo_model(frame,
                                           stream = True,
                                           device = self.device,
                                           stream_buffer = True,
                                           vid_stride = self.strides,
                                           conf = self.confidence,
                                           iou = self.iou,
                                           imgsz = (self.height, self.width),
                                           agnostic_nms = True)

                # Show camera feed
                self._showWindow(results)

    def _changeConfidence(self, new_val: int) -> None:
        """
        Callback function for confidence trackbar.

        Args:
            new_val (int): New confidence value.
        """
        self.confidence = new_val / 100.0

    def _changeIOU(self, new_val: int) -> None:
        """
        Callback function for IOU trackbar.

        Args:
            new_val (int): New IOU value.
        """
        self.iou = new_val / 100.0

    def _showWindow(self, results: list) -> None:
        """
        Show livestream with bounding boxes over detected algae.

        Args:
            results (list): Inference results.
        """
        # Create resizable, named window
        namedWindow(self.title, WINDOW_GUI_EXPANDED)

        # Create trackbars for confidence and IOU
        createTrackbar("Confidence", self.title, int(self.confidence * 100), 100, self._changeConfidence)
        createTrackbar("Intersection over Union (IoU)", self.title, int(self.iou * 100), 100, self._changeIOU)

        # Ensure confidence and IOU are at least 1 to prevent program from hanging/freezing
        setTrackbarMin("Confidence", self.title, 1)
        setTrackbarMin("Intersection over Union (IoU)", self.title, 1)
        
        for result in results:
            # Update trackbars for confidence and IOU
            getTrackbarPos("Confidence", self.title)
            getTrackbarPos("IOU", self.title)
            
            # Annotate the frame with its result, then show in window
            imshow(self.title, result.plot())

            # Exit loop if "q" is pressed
            if waitKey(1) & 0xFF == ord("q"):
                # Release webcam, if applicable
                self.camera.release()

                # Close OpenCV windows
                destroyAllWindows()
                
                exit(0)