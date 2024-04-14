from torch import device as t_device
from torch.cuda import is_available as is_cuda_available
from torch.backends.mps import is_available as is_mps_available
from ultralytics import YOLO
from os import curdir
from os.path import abspath, join
from cv2 import (VideoCapture, rectangle, putText, namedWindow, imshow,
                 waitKey, getWindowProperty, getTextSize, destroyAllWindows,
                 CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS,
                 WND_PROP_VISIBLE, FONT_HERSHEY_SIMPLEX, FILLED, LINE_AA, WINDOW_NORMAL,
                 WINDOW_FREERATIO, WINDOW_GUI_EXPANDED)

BOX_COLOR = (255, 0, 0)
FONT_COLOR = (255, 255, 255)
THICKNESS = 2
FONT_SCALE = 1
"""Bounding box attributes"""

CLASSES = [ "closterium", "microcystis", "nitzschia", "oscillatoria" ]
"""Default types of algae the model can detect"""

DEVICE = t_device("mps") if is_mps_available() else t_device("cuda") if is_cuda_available() else t_device("cpu")
"""Default device (GPU or CPU) to run algae detection model on"""

MODEL_PATH = join(abspath(curdir), "weights", "custom_yolov8x.pt")
"""Default path of custom-trained algae detection model"""

class Camera:
    def __init__(self, camera_type: str | int, title: str, classes: list[str] = CLASSES, model_path: str = MODEL_PATH, device: t_device | str = DEVICE):
        """
        Base class for camera object detection.

        Args:
            camera_type (str | int): Which camera to use. Set to streaming URL for ESP32-CAM, `0` for Webcam, `1` for iPhone.
            title (str): Window title.
            classes (list[str], optional): Types of objects the model can detect. Defaults to `CLASSES`.
            model_path (str, optional): Detection model path. Defaults to `MODEL_PATH`.
            device (device | str, optional): Device (GPU or CPU) to run detection model on. Defaults to `DEVICE`.
        """
        self.camera: VideoCapture = VideoCapture(camera_type)
        self.title: str = title
        self.classes: list[str] = classes
        self.device: t_device | str = device
        self._yolo_model: YOLO = YOLO(model_path, task = "detect")

    def run(self, width: int = 1280, height: int = 720, fps: float = 30.0):
        """
        Run camera object detection.

        Args:
            width (int, optional): Camera width. Defaults to 1280.
            height (int, optional): Camera height. Defaults to 720.
            fps (float, optional): Camera FPS. Defaults to 30.0.
        """
        # Set camera width, height, and FPS
        self.camera.set(CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(CAP_PROP_FRAME_HEIGHT, height)
        self.camera.set(CAP_PROP_FPS, fps)

        while self.camera.isOpened():
            # Fetch image from camera
            success, img = self.camera.read()

            if success:
                # Object detection
                results = self._yolo_model(img, stream = True, device = self.device, agnostic_nms = True)

                if not results: continue

                # Show camera feed
                self._showWindow(img, results)

    def _coordinates(self, img, results) -> None:
        """
        Get bounding box coordinates and dimensions.

        Args:
            img (_type_): Image of detected object.
            results (_type_): _description_
        """
        for result in results:
            for box in result.boxes:
                # Get bounding box coordinates and dimensions
                x, y, w, h = box.xyxy[0]

                # Draw bounding box
                self._drawBoundingBox(img, f"{self.classes[int(box.cls[0])]} {box.conf[0]:.2f}", int(x), int(y), int(w), int(h))

    def _showWindow(self, img, results) -> None:
        """
        Show camera feed with bounding boxes over detected objects.

        Args:
            img (_type_): Camera frame.
            results (_type_): _description_
        """
        # Coordinates
        self._coordinates(img, results)
            
        # Create resizable, named window
        namedWindow(self.title, WINDOW_NORMAL | WINDOW_FREERATIO | WINDOW_GUI_EXPANDED)

        # Show image
        imshow(self.title, img)

        # Exit loop if "q" is pressed or window is closed
        if (waitKey(1) & 0xFF == ord("q")) or (getWindowProperty(self.title, WND_PROP_VISIBLE) < 1):
            # Release webcam, if applicable
            self.camera.release()

            # Close OpenCV windows
            destroyAllWindows()
            
            exit(0)

    def _drawBoundingBox(self, img, label: str, x: int, y: int, w: int, h: int) -> None:
        """
        Draw bounding box around detected object.

        Args:
            img (_type_): Image of detected object.
            label (str): Label of detected object.
            x (int): X-coordinate of bounding box.
            y (int): Y-coordinate of bounding box.
            w (int): Width of bounding box.
            h (int): Height of bounding box.
        """
        # Bounding box frame
        rectangle(img, (x, y), (w, h), BOX_COLOR, THICKNESS)
        
        # Label
        text_width, text_height = getTextSize(label, FONT_HERSHEY_SIMPLEX, FONT_SCALE, THICKNESS)[0]
        rectangle(img, (x, y), (x + text_width, y - (text_height + 10)), BOX_COLOR, FILLED)
        putText(img, label, (x, y - 5), FONT_HERSHEY_SIMPLEX, FONT_SCALE, FONT_COLOR, THICKNESS, LINE_AA)