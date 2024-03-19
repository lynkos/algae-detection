from ultralytics import YOLO
from cv2 import rectangle, putText, namedWindow, moveWindow, imshow, getTextSize, FONT_HERSHEY_SIMPLEX, FILLED, LINE_AA
from math import ceil

# Note: If you get the following error:
# AttributeError: module 'cv2.dnn' has no attribute 'DictValue
# comment out the following (i.e., line 168) within "/Users/kiran/miniconda3/envs/algae_env/lib/python3.11/site-packages/cv2/typing/__init__.py"
# LayerId = cv2.dnn.DictValue

BOX_COLOR = (255, 0, 0)
FONT_COLOR = (255, 255, 255)
THICKNESS = 2
FONT_SCALE = 1
"""Bounding box attributes"""

CLASSES = [ "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush" ]
"""Object classes"""

MODEL = YOLO("model_weights/yolov8x.pt")
"""Model"""

def coordinates(results, img):
    for result in results:
        for box in result.boxes:
            # Get bounding box coordinates and dimensions
            x, y, w, h = box.xyxy[0]

            # Draw bounding box
            drawBoundingBox(img, f"{CLASSES[int(box.cls[0])]} {ceil((box.conf[0] * 100)) / 100}", x, y, w, h)

def showWindow(name, img, x, y):
    # Create named window
    namedWindow(name)

    # Move to (x, y)
    moveWindow(name, x, y)

    # Show image
    imshow(name, img)

def drawBoundingBox(img, text, x, y, w, h):
    # Typecast to int
    x, y, w, h = int(x), int(y), int(w), int(h)

    # Bounding box frame
    rectangle(img, (x, y), (w, h), BOX_COLOR, THICKNESS)
    
    # Label
    text_width, text_height = getTextSize(text, FONT_HERSHEY_SIMPLEX, FONT_SCALE, THICKNESS)[0]
    rectangle(img, (x, y), (x + text_width, y - (text_height + 10)), BOX_COLOR, FILLED)
    putText(img, text, (x, y - 5), FONT_HERSHEY_SIMPLEX, FONT_SCALE, FONT_COLOR, THICKNESS, LINE_AA)