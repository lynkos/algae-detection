from numpy import asarray
from cv2 import imdecode, IMREAD_COLOR # type: ignore
from requests import get
from yolo_base import showWindow, model

URL = "http://10.0.0.134/snapshot"

while(True):
    response = get(URL, stream = True).raw.read()

    if response:
        img_array = asarray(bytearray(response), dtype = "uint8")
        image = imdecode(img_array, IMREAD_COLOR)
        results = model(image)
        showWindow("ESP32 Stream", image, results)

    break