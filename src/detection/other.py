from base import Camera

CAMERA_TYPE = 1
"""Camera type: 0 = Webcam (Default), 1 = iPhone (Additional)"""

TITLE = "Webcam" if CAMERA_TYPE == 0 else "iPhone"
"""Window title"""

Camera(CAMERA_TYPE, TITLE).run()
"""Start algae detection program"""