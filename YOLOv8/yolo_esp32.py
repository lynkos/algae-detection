from numpy import asarray
from cv2 import imdecode, IMREAD_UNCHANGED, IMREAD_IGNORE_ORIENTATION # type: ignore
from requests import get
from yolo_base import showWindow, model

URL = "http://10.0.0.134/snapshot"

while(True):
    try:
        # Attempt to get image from stream
        response = get(URL, stream = True, allow_redirects = True)

        # Check if response is valid
        if response.ok:
            # Read raw data as a numpy array
            img_array = asarray(bytearray(response.raw.read()), dtype = "uint8")
            
            # Decode ndarray to OpenCV image
            image = imdecode(img_array, IMREAD_UNCHANGED | IMREAD_IGNORE_ORIENTATION)

            # Algae detection
            results = model(image)
            
            if not results: continue
            
            # Show ESP32 stream
            showWindow("ESP32 Stream", image, results)

    except: continue