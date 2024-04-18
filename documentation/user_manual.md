# User Manual
## Detect and Classify Algae
1. Open [`weights`](/weights)
2. Choose the algae detection model you want to use
   * To use your own `.pt` model, add it to [`weights`](/weights)
   * To use an existing model, decompress the `.zip` file to get the `.pt` model
      * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Nano with [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference): [`yolov8n_sahi.pt.zip`](/weights/yolov8n_sahi.pt.zip)
      * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Extra-Large: [`custom_yolov8x.pt.zip`](/weights/custom_yolov8x.pt.zip)
      * [RT-DETR](https://docs.ultralytics.com/models/rtdetr) Large: [`custom_rt-detr-l.pt.zip`](/weights/custom_rt-detr-l.pt.zip)
3. Open [`base.py`](/src/detection/base.py)
4. Set [`MODEL_PATH`](/src/detection/base.py#L19) to path of desired `.pt` model
5. Read the following depending on which camera you'll use
   * [ESP32](#esp32)
   * [Webcam and/or iPhone](#webcam-andor-iphone)

### ESP32
> [!WARNING]
> Using ESP32 as a camera requires WiFi!
>
> Unfortunately, WiFi attained via hotspots or SSOs are not compatible.
1. Click the PlatformIO icon in the activity bar, then click 'Pick a folder'
![Open PlatformIO project](/src/assets/esp32/setup/platformio_folder.png)
2. Open [`streaming`](/src/streaming)
![Open `streaming`](/src/assets/esp32/setup/open_streaming.png)
3. Make sure the ESP32 is connected to the computer
4. Configure ESP32 for streaming
   - Click 'Build' to compile the code
   - Click 'Upload' to flash the code to ESP32
   - Click 'Monitor' for real-time logging in terminal (particularly helpful when troubleshooting)
   ![Build, Upload, Monitor](/src/assets/esp32/setup/build_upload_monitor.png)
5. Go to your WiFi settings and select the network starting with `ESP32CAM-RTSP`
![`ESP32CAM-RTSP` network](/src/assets/esp32/setup/choose_ap.png)
6. Once a window automatically pops up, click 'Change settings'
![Window popup](/src/assets/esp32/setup/ap_popup.png)
7. You must fill in each of the following:
   - AP (i.e., Access Point) password
   - WiFi SSID
   - WiFi password (if applicable)
![Change settings](/src/assets/esp32/setup/init_config.png)
8. Change any of the other settings (you can always change them again), then click 'Apply'
![Apply](/src/assets/esp32/setup/apply.png)
9. Disconnect from the current network and reconnect to your WiFi
![Disconnect](/src/assets/esp32/setup/disconnect.png)
10. You can now connect to and stream from the ESP32 at the HTTP address listed under 'Special URLs / API'
![Stream](/src/assets/esp32/setup/get_url.png)
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
14. See [this specific `README.md`](/src/streaming/README.md) for further details

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
> [!NOTE]
> All algae detection models trained, validated, and tested for this project are fine-tuned (with the [algae dataset](https://drive.google.com/drive/folders/1gd85o6dpcjDwWJUUi4x9slhjHHuoY4K0)) versions of the following pre-trained models:
> - [YOLOv8](https://docs.ultralytics.com/models/yolov8)
> - [RT-DETR](https://docs.ultralytics.com/models/rtdetr)
> - [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference)

1. Visit [this Google Colab notebook](https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ)
2. Follow the notebook's instructions
3. Run notebook