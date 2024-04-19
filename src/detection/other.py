from base import Camera

CAMERA_TYPE = 1
"""Camera type: 0 = Webcam (Default), 1 = iPhone (Additional)"""

TITLE = "Webcam" if CAMERA_TYPE == 0 else "iPhone"
"""Window title"""

Camera(CAMERA_TYPE, TITLE, width = 320, height = 320).run()
"""Start algae detection program"""