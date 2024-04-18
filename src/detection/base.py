from torch import device
from torch.cuda import is_available as is_cuda_available
from torch.backends.mps import is_available as is_mps_available
from ultralytics import YOLO
from os import curdir
from os.path import abspath, join
from cv2 import (VideoCapture, namedWindow, imshow, waitKey, getWindowProperty,
                 destroyAllWindows, WND_PROP_VISIBLE, WINDOW_GUI_EXPANDED,
                 CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS)

WIDTH: int = 1280
HEIGHT: int = 720
FPS: float = 30.0
"""Default camera attributes"""

DEVICE: device = device("mps") if is_mps_available() else device("cuda") if is_cuda_available() else device("cpu")
"""Default device (GPU or CPU) to run detection model on"""

MODEL_PATH: str = join(abspath(curdir), "weights", "yolov8n_sahi.pt")
"""Default path of custom-trained algae detection model"""

CONFIDENCE: float = 0.25
"""Default confidence threshold of detection model"""

class Camera:
    def __init__(self,
                 camera_type: str | int,
                 title: str = "Algae Detector",
                 model_path: str = MODEL_PATH,
                 confidence: float = CONFIDENCE,
                 device_type: device | str = DEVICE,
                 width: int = WIDTH,
                 height: int = HEIGHT,
                 fps: float = FPS):
        """
        Base class for camera object detection.

        Args:
            camera_type (str | int): Which camera to use. Set to streaming URL for ESP32-CAM, `0` for Webcam, `1` for iPhone.
            title (str, optional): Window title. Defaults to "Algae Detector".
            model_path (str, optional): Detection model's path. Defaults to `MODEL_PATH`.
            confidence (float, optional): Detection model's confidence threshold. Defaults to `CONFIDENCE`.
            device_type (device | str, optional): Device (GPU or CPU) to run detection model on. Defaults to `DEVICE`.
            width (int, optional): Camera width. Defaults to `WIDTH`.
            height (int, optional): Camera height. Defaults to `HEIGHT`.
            fps (float, optional): Camera FPS. Defaults to `FPS`.
        """
        self.camera: VideoCapture = VideoCapture(camera_type)
        self.camera.set(CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(CAP_PROP_FRAME_HEIGHT, height)
        self.camera.set(CAP_PROP_FPS, fps)
        self.title: str = title
        self._yolo_model: YOLO = YOLO(model_path, task = "detect")
        self.confidence: float = confidence
        self.device: device | str = device_type

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
                                           vid_stride = 5,
                                           conf = self.confidence,
                                           iou = 0.5,
                                           agnostic_nms = True)

                if not results: continue

                # Show camera feed
                self._showWindow(results)

    def _showWindow(self, results: list) -> None:
        """
        Show camera feed with bounding boxes over detected objects.

        Args:
            results (list): Inference results.
        """
        # Create resizable, named window
        namedWindow(self.title, WINDOW_GUI_EXPANDED)
        
        for result in results:
            # Annotate the frame with its result, then show in window
            imshow(self.title, result.plot())

            # Exit loop if "q" is pressed or window is closed
            if (waitKey(1) & 0xFF == ord("q")) or (getWindowProperty(self.title, WND_PROP_VISIBLE) < 1):
                # Release webcam, if applicable
                self.camera.release()

                # Close OpenCV windows
                destroyAllWindows()
                
                exit(0)