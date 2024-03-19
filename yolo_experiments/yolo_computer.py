from cv2 import VideoCapture, waitKey, destroyAllWindows, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
from yolo_base import MODEL, coordinates, showWindow

# Original versions:
# opencv: 4.6.0
# opencv-python: 4.8.1.

# Start webcam
WEBCAM = VideoCapture(0) # VideoCapture(URL)
WEBCAM.set(CAP_PROP_FRAME_WIDTH, 1280)
WEBCAM.set(CAP_PROP_FRAME_HEIGHT, 720)

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
        showWindow("Webcam", img, 0, 0)

    else: break

    # Check for key press, if "q" is pressed, exit the loop
    if waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
WEBCAM.release()

# Close OpenCV windows
destroyAllWindows()

exit(0)