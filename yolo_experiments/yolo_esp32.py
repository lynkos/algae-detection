from requests import get
from numpy import uint8, array
from cv2 import imdecode, imshow, waitKey, destroyAllWindows
from yolo_base import URL, MODEL, coordinates

while True:    
    # Fetch image from URL
    response = get(URL, stream = True)
    print("Got Content!")
    
    if response.status_code == 200:        
        # Read the image as a numpy array (takes the most time)
        img_array = array(bytearray(response.content), dtype = uint8)
        
        # Decode the numpy array to an OpenCV image
        img = imdecode(img_array, -1)
        
        # Object detection code
        results = MODEL(img, stream = True)

        # Coordinates
        coordinates(results, img)

        # Show ESP32 stream
        imshow("Video Stream", img)

    # Check for key press, if "q" is pressed, exit the loop
    if waitKey(1) & 0xFF == ord("q"):
        break

# Close OpenCV windows
destroyAllWindows()