from numpy import uint8, array
from cv2 import imdecode
from urllib import request
from PIL import Image
from yolo_base import MODEL, showWindow

URL = "http://10.0.0.134/cam-lo.jpg"

while True:    
    # Fetch image from URL
    img_array = request.urlopen(URL)

    # Read the image as a numpy array (takes the most time)
    img_array = array(Image.fromarray(img_array, "RGB"))
    #img_array = array(bytearray(img_array.read()), dtype = uint8)

    # Decode the numpy array to an OpenCV image
    img = imdecode(img_array, -1)

    # Object detection code
    results = MODEL(img, stream = True, device = "mps", agnostic_nms = True)

    # Show ESP32 stream (processing done here)
    showWindow("ESP32 Stream", img, results)