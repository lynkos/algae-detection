# User Manual
## Run the ESP32 Camera Web Server with YOLO on Computer
1. Open Arduino IDE and connect ESP32 chip. Make sure the correct board and port are selected.
2. Open `sketch_jan17a.ino`, then click Upload. This will start the camera and the web server.
3. Wait for it to upload. When it's finished, it should produce an output similar to:
```
CAMERA OK
http://10.1.10.134
  /cam-lo.jpg
  /cam-hi.jpg
  /cam-mid.jpg
```
4. Choose which quality of image you want to use for the inference. The options are low, medium, and high quality. The low quality image is the smallest and fastest to process, but it is also the lowest resolution. The high quality image is the largest and slowest to process, but it is also the highest resolution. The medium quality image is in between the low and high quality images in terms of size, speed, and resolution.
5. Open the link in a browser to make sure it's working. If it is, you should see a live video feed from the camera.
6. Navigate to `yolo_experiments`. If you want to run the inference on your computer, open `yolo_computer.py`. If you want to run the inference on the ESP32, open `yolo_esp32.py`.
7. Change the `url` variable to the link you got from the serial monitor.
8. Run the script. It should open to a window with the live video feed from the camera.
9. Press `q` or `CTRL + C` to stop the script and close the window.

## Running Model Deplyment on the Chip
Once you have gone thought the instalation guide for the Model Deployment Program you can run the ESP-IDF 5.0 CMD as shown bellow and run the following comands to make an inference on a hardcoded rest image.

Make sure you are in the model_deployment directory
```Bash
cd model_deployment
```

Make sure that COMX is the current port that your ESP32 Chip is connected too i.e. COM5
```
idf.py set-target esp32
```
Check if the flash is configured to 4MB by typing 
```
idf.py menuconfig
```

Then compline and run by doing the following.
```
idf.py build
idf.py -p COMX flash
idf.py -p COMX monitor
```
![](./_static/idf-cmd.png)

## How to Change The Sample Image
You can generate new example images that you can classify directly on the chip by doing the following.
Run the notebook found in model_deployment and scroll to the bottom of the notbook under the heading "Testing". There is some code there you can run to turn an image at the index you desire into a C++ array which you can copy and past it as the example image in the model_deployment program.

![](./_static/gen_example.png)

This is how the output would look like from the google notebook. The C++ array generated are the numbers you see above the image.

To save this as an example image that the chip can classify you would take this C++ array and paste it here so that example_element[] is now equal to the new array you generated.

![](./_static/deploy_img.png)

## How to Run The Webserver
- First make sure that your ESP-32 chip is mounted onto the microscope and that it is connected to your local computer through a USB cable.

- To run the camera-web server onto the chip you would need to download the Arduino IDE to compile and flash the web server code onto the chip. You can install Arduino IDE from https://www.arduino.cc/en/software

- Go to file, preferences, and add the additional board manager url https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

![](./_static/adrino_ide_preferences.png)

![](./_static/arduino_url.png)
    
- To download the camera web server code you can clone our repository to access it https://github.com/rdgbrian/cap-2-project-algea-detection, and open the webserver code in your IDE. Or alternatively you can access it though the IDE. You can access it though the IDE by setting the current board to be the ESP32 Dev Module. Then selecting file->examples->ESP32->Camera->CameraWebServer

![](./_static/camera_server.png)

Once selected be sure to use the AI Thinker model and not the ESP 32 Eye cam model: 

![](./_static/corrected_web.png)

You will then need to fill out the required credentials which will be the internet connection name under ssid and password under the password

![](./_static/wifi_pwd.png)

- Once you are ready to run your program. Check if the correct bord and port (USB connection) is selected by pressing the button that has the usb symbol in the top middle of your screen.

![](./_static/port_chip.png)
    
- Then compline and flash your code onto the chip.
Open the serial monitor in the IDE to see the input from the chip. This input  will provide a link to access the live camera input. Copy and paste this link onto your browser to interact and view the live video.