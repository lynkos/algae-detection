from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
from yolo_base import MODEL, coordinates

# Original versions:
# opencv: 4.6.0
# opencv-python: 4.8.1.

CONNECTION_TYPE = 0
"""0 for computer's webcam, 1 for external webcam (i.e., iPhone camera)"""

# Start webcam
WEBCAM = VideoCapture(CONNECTION_TYPE) # VideoCapture(URL)
WEBCAM.set(CAP_PROP_FRAME_WIDTH, 640)
WEBCAM.set(CAP_PROP_FRAME_HEIGHT, 480)

while WEBCAM.isOpened():
    print("Webcam started!")
    
    # Fetch image from webcam
    success, img = WEBCAM.read()

    if success:
        # Object detection code
        results = MODEL(img, stream = True, device = "mps", agnostic_nms = True)

        if not results: continue

        # Coordinates
        coordinates(results, img)

        # Show webcam feed
        imshow("Webcam", img)

    else: break

    # Check for key press, if "q" is pressed, exit the loop
    if waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
WEBCAM.release()

# Close OpenCV windows
destroyAllWindows()