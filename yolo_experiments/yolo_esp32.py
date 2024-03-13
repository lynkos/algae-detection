import cv2
import requests
import numpy as np
from ultralytics import YOLO
import cv2
import math 
import time


url = "http://10.0.0.134/cam-hi.jpg"
# model
model = YOLO("yolo-Weights/yolov8n.pt") #8n.pt
print("Model Loaded!")
# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

while True:
    # Fetch the image from the URL
    start = time.time()
    response = requests.get(url, stream=True)
    end = time.time()
    print("Got Content!",response.status_code, "Time: ", end-start)
    if response.status_code == 200:
        # Read the image as a numpy array
        start = time.time()
        img_array = np.array(bytearray(response.content), dtype=np.uint8)
        # Decode the numpy array to an OpenCV image
        img = cv2.imdecode(img_array, -1)
        end = time.time()
        print("Process Img:", end-start)
        # Display the image

        # object detection code

        print("Making Prediction")
        results = model(img, stream=True)

        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = math.ceil((box.conf[0]*100))/100
                print("Confidence --->",confidence)

                # class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)


        cv2.imshow('Video Stream', img)

    # Check for key press, if 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close OpenCV windows
cv2.destroyAllWindows()
