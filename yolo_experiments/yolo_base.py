from ultralytics import YOLO
from cv2 import rectangle, putText, FONT_HERSHEY_SIMPLEX
from math import ceil

# Note: If you get the following error:
# AttributeError: module 'cv2.dnn' has no attribute 'DictValue
# comment out the following (i.e., line 168) within "/Users/kiran/miniconda3/envs/algae_env/lib/python3.11/site-packages/cv2/typing/__init__.py"
# LayerId = cv2.dnn.DictValue

# Object classes
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

URL = "http://10.0.0.134/cam-lo.jpg"
MODEL = YOLO("yolo-Weights/yolov8n.pt") #YOLO("/Users/kiran/Documents/workspace/Projects/algae-detection/model_development/model.keras")
print("Model Loaded!")

def coordinates(results, img):
    # Coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]

            # Convert to int values
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Put box in cam
            rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Confidence
            confidence = ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Class name
            cls = int(box.cls[0])
            print("Class name -->", CLASSES[cls])

            # Object details
            org = [x1, y1]
            font = FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            putText(img, CLASSES[cls], org, font, fontScale, color, thickness)