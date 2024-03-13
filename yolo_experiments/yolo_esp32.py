from requests import get
from numpy import uint8, array
from ultralytics import YOLO
from cv2 import imdecode, imshow, waitKey, destroyAllWindows
from time import time
from yolo_base import coordinates

URL = "http://10.0.0.134/cam-hi.jpg"
MODEL = YOLO("yolo-Weights/yolov8n.pt") #8n.pt

print("Model Loaded!")

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

while True:
    start = time()
    
    # Fetch image from URL
    response = get(URL, stream = True)
    
    end = time()
    
    print("Got Content!", response.status_code, "Time:", end - start)
    
    if response.status_code == 200:
        start = time()
        
        # Read the image as a numpy array (takes the most time)
        img_array = array(bytearray(response.content), dtype = uint8)
        
        # Decode the numpy array to an OpenCV image
        img = imdecode(img_array, -1)
        
        end = time()
        
        print("Image Processing Time:", end - start)
        # Display the image

        # Object detection code
        print("Making Prediction...")
        results = MODEL(img, stream = True)

        # Coordinates
        coordinates(results, img)

        imshow("Video Stream", img)

    # Check for key press, if "q" is pressed, exit the loop
    if waitKey(1) & 0xFF == ord("q"):
        break

# Close OpenCV windows
destroyAllWindows()