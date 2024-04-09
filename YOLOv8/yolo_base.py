from torch import device
from torch.cuda import is_available as is_cuda_available
from torch.backends.mps import is_available as is_mps_available
from ultralytics import YOLO
from math import ceil
from cv2 import (rectangle, putText, namedWindow, moveWindow, imshow, waitKey, # type: ignore
                 getWindowProperty, getTextSize, destroyAllWindows, # type: ignore
                 WND_PROP_VISIBLE, FONT_HERSHEY_SIMPLEX, FILLED, LINE_AA) # type: ignore

# Note: If you get the following error:
# AttributeError: module 'cv2.dnn' has no attribute 'DictValue
# comment out the following (i.e., line 168) within "/Users/kiran/miniconda3/envs/algae_env/lib/python3.11/site-packages/cv2/typing/__init__.py"
# LayerId = cv2.dnn.DictValue

BOX_COLOR = (255, 0, 0)
FONT_COLOR = (255, 255, 255)
THICKNESS = 2
FONT_SCALE = 1
"""Bounding box attributes"""

CLASSES = [ "closterium", "microcystis", "nitzschia", "oscillatoria" ]
"""Object classes"""

DEVICE = device("mps") if is_mps_available() else device("cuda") if is_cuda_available() else device("cpu")
"""Model device (GPU or CPU)"""

WEIGHTS = "model_weights/best_sahi_v1.pt"
"""Model weights"""

MODEL = YOLO(WEIGHTS, task = "detect")
"""Model"""

def coordinates(img, results):
    for result in results:
        for box in result.boxes:
            # Get bounding box coordinates and dimensions
            x, y, w, h = box.xyxy[0]

            # Draw bounding box
            drawBoundingBox(img, f"{CLASSES[int(box.cls[0])]} {ceil((box.conf[0] * 100)) / 100}", x, y, w, h)

def model(img):
    return MODEL(img, stream = True, device = DEVICE, agnostic_nms = True)

def showWindow(name, img, results, cam = None, x = 0, y = 0):
    # Coordinates
    coordinates(img, results)
        
    # Create named window
    namedWindow(name)

    # Move to (x, y)
    moveWindow(name, x, y)

    # Show image
    imshow(name, img)

    # Exit loop if "q" is pressed or window is closed
    if (waitKey(1) & 0xFF == ord("q")) or (getWindowProperty(name, WND_PROP_VISIBLE) < 1):
        # Release webcam, if applicable
        if cam: cam.release()

        # Close OpenCV windows
        destroyAllWindows()
        
        exit(0)

def drawBoundingBox(img, text, x, y, w, h):
    # Typecast to int
    x, y, w, h = int(x), int(y), int(w), int(h)

    # Bounding box frame
    rectangle(img, (x, y), (w, h), BOX_COLOR, THICKNESS)
    
    # Label
    text_width, text_height = getTextSize(text, FONT_HERSHEY_SIMPLEX, FONT_SCALE, THICKNESS)[0]
    rectangle(img, (x, y), (x + text_width, y - (text_height + 10)), BOX_COLOR, FILLED)
    putText(img, text, (x, y - 5), FONT_HERSHEY_SIMPLEX, FONT_SCALE, FONT_COLOR, THICKNESS, LINE_AA)