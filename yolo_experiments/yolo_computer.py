from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows
from yolo_base import MODEL, coordinates

# Original versions:
# opencv: 4.6.0
# opencv-python: 4.8.1.

# Start webcam
WEBCAM = VideoCapture(0) # VideoCapture(URL)
WEBCAM.set(3, 640)
WEBCAM.set(4, 480)
print("Webcam started!")

while True:
    # Fetch image from webcam
    success, img = WEBCAM.read()
    print("Success:", success, "Image:", type(img))

    # Object detection code
    print("Making Prediction...")
    results = MODEL(img, stream = True)

    # Coordinates
    coordinates(results, img)

    # Show webcam feed
    imshow("Webcam", img)

    # Check for key press, if "q" is pressed, exit the loop
    if waitKey(1) == ord('q'):
        break

# Release webcam
WEBCAM.release()

# Close OpenCV windows
destroyAllWindows()