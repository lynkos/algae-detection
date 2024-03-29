from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS
from yolo_base import showWindow, MODEL

WEBCAM = VideoCapture(0) # VideoCapture(URL)
"""Start webcam"""

WIDTH = 1280
HEIGHT = 720
FPS = 30.0
"""Webcam attributes"""

WEBCAM.set(CAP_PROP_FRAME_WIDTH, WIDTH)
WEBCAM.set(CAP_PROP_FRAME_HEIGHT, HEIGHT)
WEBCAM.set(CAP_PROP_FPS, FPS)
"""Set webcam width, height, and FPS"""

while WEBCAM.isOpened():
    # Fetch image from webcam
    success, img = WEBCAM.read()

    if success:
        # Object detection
        results = MODEL(img, stream = True, device = "mps", agnostic_nms = True)

        if not results: continue

        # Show webcam feed
        showWindow("Webcam", img, results, WEBCAM)