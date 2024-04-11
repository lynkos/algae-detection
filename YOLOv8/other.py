from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS
from base import showWindow, model

CAMERA_TYPE = 0
"""Camera type: 0 = Webcam (Default), 1 = iPhone (Additional)"""

CAMERA = VideoCapture(CAMERA_TYPE)
"""Initialize camera"""

TITLE = "Webcam" if CAMERA_TYPE == 0 else "iPhone"
WIDTH = 1280
HEIGHT = 720
FPS = 30.0
"""Camera attributes"""

CAMERA.set(CAP_PROP_FRAME_WIDTH, WIDTH)
CAMERA.set(CAP_PROP_FRAME_HEIGHT, HEIGHT)
CAMERA.set(CAP_PROP_FPS, FPS)
"""Set camera width, height, and FPS"""

while CAMERA.isOpened():
    # Fetch image from camera
    success, img = CAMERA.read()

    if success:
        # Object detection
        results = model(img)

        if not results: continue

        # Show camera feed
        showWindow(TITLE, img, results, CAMERA)