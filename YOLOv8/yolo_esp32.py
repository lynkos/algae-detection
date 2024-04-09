from numpy import uint8, array
from cv2 import imdecode
from urllib import request
from PIL.Image import fromarray
from yolo_base import showWindow, model

URL = "http://10.0.0.134/cam-lo.jpg"

while True:    
    # Fetch image from URL
    img_array = request.urlopen(URL)

    # Read the image as a numpy array (takes the most time)
    img_array = array(fromarray(img_array, "RGB"))
    #img_array = array(bytearray(img_array.read()), dtype = uint8)

    # Decode the numpy array to an OpenCV image
    img = imdecode(img_array, -1)

    # Object detection code
    results = model(img)

    # Show ESP32 stream (processing done here)
    showWindow("ESP32 Stream", img, results)

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video file
video_path = "path/to/your/video/file.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)