# User Manual
## Detect and Classify Algae
1. Open [`weights`](/weights)
2. Choose the algae detection model you want to use

> [!TIP]
> To use your own `.pt` model, add it to [`weights`](/weights).
>
> To use an existing model, decompress the `.zip` file to get the `.pt` model.
> * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Nano with [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference): [`yolov8n_sahi.pt.zip`](/weights/yolov8n_sahi.pt.zip)
> * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Extra-Large: [`custom_yolov8x.pt.zip`](/weights/custom_yolov8x.pt.zip), [`custom_yolov8x_v2.pt.zip`](/weights/custom_yolov8x_v2.pt.zip)

3. Open [`base.py`](/src/detection/base.py)
4. Set [`MODEL_PATH`](/src/detection/base.py#L20) to path of desired `.pt` model
5. Read the following depending on which camera you'll use
   * [ESP32](#esp32)
   * [Webcam and/or iPhone](#webcam-andor-iphone)

### ESP32
> [!WARNING]
> Current implementation of ESP32-CAM requires WiFi!
>
> Unfortunately, WiFi connections from hotspots or SSOs are not compatible.

1. Click the PlatformIO icon in the activity bar, then click 'Pick a folder'
   ![Open PlatformIO project](/src/assets/esp32/platformio_folder.png)
2. Open [`streaming`](/src/streaming)
   ![Open `streaming`](/src/assets/esp32/open_streaming.png)
3. Make sure the ESP32 is connected to the computer
4. Build and upload ESP32 for streaming
   - Click 'Build' to compile code
   - Click 'Upload' to flash code to ESP32
   - OPTIONAL: Click 'Monitor' for real-time logging in terminal (helpful for troubleshooting)
   ![Build, Upload, Monitor](/src/assets/esp32/build_upload_monitor.png)
5. To connect initially to the device, connect to the WiFi network starting with `ESP32CAM-RTSP`
   ![`ESP32CAM-RTSP` network](/src/assets/esp32/choose_ap.png)
6. Click 'Change settings' once the browser automatically opens the home page ([`http://192.168.4.1`](http://192.168.4.1))
   ![Window popup](/src/assets/esp32/ap_popup.png)
7. You **must** fill in each of the following fields:
   - AP (i.e., Access Point) password
   - WiFi SSID
   - WiFi password (if applicable)

> [!TIP]
> If you ever lose/forget the AP password, click 'Erase flash' (in PlatformIO's extension UI) to erase and reset the device, then follow steps 4 and onwards again.

![System config](/src/assets/esp32/init_config.png)

8. Update the camera settings if you wish (you can always change them later), then scroll down and click 'Apply'

> [!WARNING]
> Very low number for 'JPG quality' (i.e., very high quality) can cause the ESP32 to crash or return no image!

![Camera Settings](/src/assets/esp32/config.png)

10. Disconnect from the current network and reconnect to your WiFi in order to reset ESP32 (so the settings take effect) and connect to the AP

> [!TIP]
> If the error screen says it's unable to make a connection, try rebooting the device first (you can do so manually by pressing the 'Reset' button). The device will wait 30 seconds for a connection (configurable).
>
> Connect to the SSID, go to the device's IP address and, anytime you're prompted for credentials, enter `admin` as the username and the AP password for the password.
<!-- Img of reset button on ESP32 -->

![Disconnect](/src/assets/esp32/disconnect.png)

10. You can now configure and stream from the ESP32 via HTTP

> [!WARNING]
> Anyone with network access to the device can see the streams and images!

![Home Page](/src/assets/esp32/index.png)

11. Open [`esp32.py`](/src/detection/esp32.py) once finished
12. Set [`URL`](/src/detection/esp32.py#L3) to ESP32's IP address (i.e., `http://10.0.0.114` in this example)
13. Run [`esp32.py`](/src/detection/esp32.py)
   * POSIX
      ```
      $(which python) src/detection/esp32.py
      ```
   * Windows
      ```
      $(where python) src\detection\esp32.py
      ```
14. See [this repo's `README.md`](https://github.com/rzeldent/esp32cam-rtsp) for further details

### Webcam and/or iPhone
1. Open [`other.py`](/src/detection/other.py)
2. Set [`CAMERA_TYPE`](/src/detection/other.py#L3) to `0` to use webcam or `1` to use iPhone
3. Run [`other.py`](/src/detection/other.py)
   * POSIX
      ```
      $(which python) src/detection/other.py
      ```
   * Windows
      ```
      $(where python) src\detection\other.py
      ```

## Training, Validating, and Testing Model
1. Visit [this Google Colab notebook](https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ)
2. Follow the notebook's instructions
3. Run notebook