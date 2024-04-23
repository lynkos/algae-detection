# User Manual
## Detect and Classify Algae
<details open>
   <summary><b>User Interface</b></summary>
   <img align="center" alt="User Interface" src="/src/assets/user_interface.png">
</details>

1. Open [`weights`](/weights)
2. Choose the algae detection model you want to use

> [!TIP]
> To use your own `.pt` model, add it to [`weights`](/weights).
>
> To use an existing model, decompress the `.zip` file to get the `.pt` model.
> * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Nano with [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference): [`yolov8n_sahi.pt.zip`](/weights/yolov8n_sahi.pt.zip)
> * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Extra-Large: [`custom_yolov8x.pt.zip`](/weights/custom_yolov8x.pt.zip), [`custom_yolov8x_v2.pt.zip`](/weights/custom_yolov8x_v2.pt.zip)

3. Open [`base.py`](/src/detection/base.py)
4. Set [`MODEL_PATH`](/src/detection/base.py#L22) to path of desired `.pt` model
5. Read the following depending on which camera you'll use
   * [ESP32](#esp32)
   * [iPhone](#iphone)
   * [Webcam](#webcam)

### ESP32
> [!IMPORTANT]
> Current implementation **requires** WiFi!
>
> This is because the ESP32-CAM livestreams to an [MJPEG server](https://en.wikipedia.org/wiki/Motion_JPEG#Video_streaming) over HTTP, which is how [`esp32.py`](/src/detection/esp32.py) gets the camera input.
>
> Unfortunately, WiFi connections from hotspots or SSOs are — in my experience — incompatible.

1. Click the PlatformIO icon in the activity bar, then click 'Pick a folder'<br>
   <img alt="Open PlatformIO project" height="350" src="/src/assets/esp32/platformio_folder.png">
2. Open [`streaming`](/src/streaming)<br>
   <img alt="Open `streaming`" height="350" src="/src/assets/esp32/open_streaming.png">
3. Make sure the ESP32 is connected to the computer
4. Build and upload code to ESP32
   - Click 'Build' to compile code
   - Click 'Upload' to flash code to ESP32<br>
   <img alt="Build, Upload, Monitor" height="350" src="/src/assets/esp32/build_upload_monitor.png">
5. To connect initially to the device, connect to the WiFi network starting with `ESP32CAM-RTSP`<br>
   <img alt="`ESP32CAM-RTSP` network" height="250" src="/src/assets/esp32/choose_ap.png">
6. Click 'Change settings' once the browser automatically opens the home page ([`http://192.168.4.1`](http://192.168.4.1))

<img alt="Window popup" height="350" src="/src/assets/esp32/ap_popup.png">

7. You **must** fill in all of the following fields:
   - AP (i.e., Access Point) password
   - WiFi SSID
   - WiFi password (if applicable)

> [!NOTE]
> If you ever lose/forget the AP password, click 'Erase flash' (in PlatformIO's extension UI) to erase and reset the device, then follow steps 4 and onwards again.

<img alt="System config" height="350" src="/src/assets/esp32/init_config.png">

8. Update the server settings and configure camera options (you can always change them later)

> [!WARNING]
> Very low number for 'JPG quality' (i.e., very high quality) may cause the ESP32 to crash or return no image!

   <details>
      <summary><b>Camera Settings</b></summary>
      <div align="center"><img alt="Camera Settings" src="/src/assets/esp32/config.png"></div>
   </details>

9. Scroll down and click 'Apply' to save settings

> [!IMPORTANT]
> You must reset the ESP32 everytime you change the settings for it to take effect.

10. Disconnect from the current network and reconnect to your WiFi in order to reset ESP32 and connect to the AP

> [!NOTE]
> If there's an error screen saying it's unable to make a connection, try rebooting the ESP32 first (you can do so manually by pressing the 'Reset' button). It'll wait 30 seconds for a connection (can be changed in system configuration's 'Startup delay (seconds)' setting, shown in Step #7).
>
> Connect to the SSID, go to the ESP32's IP address and enter your credentials:
> - Username: `admin`
> - Password: AP password from Step #7

<img alt="Disconnect" height="350" src="/src/assets/esp32/disconnect.png">

11. Go back to PlatformIO's VSCode extension and click 'Monitor', then search for the ESP32's IP address

> [!TIP]
> To quickly find the IP address:
> - PC
>   ```
>   Ctrl + F
>   ```
> - Mac
>   ```
>   ⌘ + F
>   ```
>
> Then type 'IP Address' in the search bar and press 'Enter'.

<img alt="IP Address" src="/src/assets/esp32/esp32_ip.png">

12. You can now stream from the ESP32
   - HTTP Motion JPEG Streamer: `http://<ESP32 IP address>/stream`
   - HTTP Image: `http://<ESP32 IP address>/snapshot`
   - RTSP: `rtsp://<ESP32 IP address>:554/mjpeg/1`

> [!CAUTION]
> Anyone with network access to the device can see the streams and images!

   <details>
      <summary><b>Home Page</b></summary>
      <div align="center"><img alt="Home Page" src="/src/assets/esp32/index.png"></div>
   </details>

13. Open [`esp32.py`](/src/detection/esp32.py) once finished
14. Set [`URL`](/src/detection/esp32.py#L3) to ESP32's IP address (i.e., `http://10.0.0.111` in this example)
15. Run [`esp32.py`](/src/detection/esp32.py)
   * POSIX
      ```sh
      $(which python) src/detection/esp32.py
      ```
   * Windows
      ```sh
      $(where python) src\detection\esp32.py
      ```

> [!NOTE]
> See [this module's](https://github.com/rzeldent/esp32cam-rtsp) [`README.md`](https://github.com/rzeldent/esp32cam-rtsp/blob/main/README.md) for further details on streaming.
>
> To update to latest version, commit and push changes, then run the following command in the terminal:
> <pre>git subtree pull --prefix src/streaming https://github.com/rzeldent/esp32cam-rtsp.git develop --squash</pre>

### iPhone
1. Open [`iphone.py`](/src/detection/iphone.py)
2. Run [`iphone.py`](/src/detection/iphone.py)
   * POSIX
      ```sh
      $(which python) src/detection/iphone.py
      ```
   * Windows
      ```sh
      $(where python) src\detection\iphone.py
      ```
3. If successfully connected, your iPhone's screen should look like this:
   ![iPhone connected](/src/assets/iphone/iphone_ui_connect.png)
4. Press `q` on your computer or 'Disconnect' on your iPhone to exit the program
   ![iPhone disconnected](/src/assets/iphone/iphone_ui_disconnect.png)

### Webcam
1. Open [`webcam.py`](/src/detection/webcam.py)
2. Run [`webcam.py`](/src/detection/webcam.py)
   * POSIX
      ```sh
      $(which python) src/detection/webcam.py
      ```
   * Windows
      ```sh
      $(where python) src\detection\webcam.py
      ```

## Training, Validating, and Testing Model
1. Visit [this Google Colab notebook](https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ)
2. Follow the notebook's instructions
3. Run notebook