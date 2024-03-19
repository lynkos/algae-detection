from numpy import uint8, array
from cv2 import imdecode, waitKey, destroyAllWindows
from yolo_base import MODEL, coordinates, showWindow
from urllib import request

URL = "http://10.0.0.134/cam-lo.jpg"

while True:    
    # Fetch image from URL
    img_array = request.urlopen(URL)

    # Read the image as a numpy array (takes the most time)
    img_array = array(bytearray(img_array.read()), dtype = uint8)

    # Decode the numpy array to an OpenCV image
    img = imdecode(img_array, -1)

    # Object detection code
    results = MODEL(img, stream = True, device = "mps", agnostic_nms = True)

    # Coordinates
    coordinates(results, img)

    # Show ESP32 stream (processing done here)
    showWindow("ESP32 Stream", img, 0, 0)
    
    # Exit loop and close OpenCV window(s) when "q" is pressed
    if waitKey(1) & 0xFF == ord("q"):
        destroyAllWindows()
        exit(0)