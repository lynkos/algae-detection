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

3. Open [`Camera.py`](/src/detection/Camera.py)
4. Set [`MODEL_PATH`](/src/detection/Camera.py#L25) to path of desired `.pt` model
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
3. Connect the ESP32 to your computer with the Micro-USB cable, then select its board type and USB port at the bottom of the window<br>
   <img alt="Select board and port" src="/src/assets/esp32/board_port.png">
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
> You must reset the ESP32 (i.e., press its 'Reset' button) everytime you change the settings for it to take effect.

10. Disconnect from the current network and reconnect to your WiFi in order to reset ESP32 and connect to the AP

> [!NOTE]
> If there's an error screen saying it's unable to make a connection, try resetting the ESP32 first. It'll wait 30 seconds for a connection (can be changed in system configuration's 'Startup delay (seconds)' setting, shown in Step #7).
>
> Connect to the SSID, go to the ESP32's IP address and enter your credentials:
> - Username: `admin`
> - Password: AP password from Step #7

<img alt="Disconnect" height="350" src="/src/assets/esp32/disconnect.png">

11. Go back to PlatformIO and click 'Monitor' to determine the ESP32's IP address

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
>
> <img alt="IP Address" src="/src/assets/esp32/esp32_ip.png">

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
> See [this module](https://github.com/rzeldent/esp32cam-rtsp)'s [`README.md`](https://github.com/rzeldent/esp32cam-rtsp/blob/main/README.md) for further details on streaming.
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
4. Press 'Escape' on your computer or 'Disconnect' on your iPhone to exit the program
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

## Train, Validate, and Test Model
1. Visit [this Google Colab notebook](https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ)
2. Follow the notebook's instructions
3. Run notebook

## Glossary
1. **Access Point (AP)**: Networking device that allows wireless-capable devices to connect to a WLAN; in this case, it provides WiFi to ESP32
2. **Algae**: Group of mostly aquatic, photosynthetic, and nucleus-bearing organisms that lack many features of larger multicellular plants
3. **Anaconda**: Open-source platform for managing and installing various Python packages
4. **Artificial Intelligence (AI)**: Simulation of human intelligence in machines that can perform tasks like problem-solving, decision-making, learning, etc.
5. **Deep Neural Network (DNN)**: ML method inspired by the human brain’s neural structure that can recognize complex patterns in data (e.g., pictures, text, sounds, etc.) to produce accurate insights and predictions
6. **Closterium**: Type of algae identified by their elongated or crescent shape
7. **Computer Vision (CV)**: Field of computer science that focuses on enabling computers to identify and understand objects and people in images and videos
8. **Confusion Matrix**: Visualizes model performance (i.e., number of correct and incorrect predictions per class), where the x-axis is the true value and y-axis is the model’s predicted value; diagonal elements represent the number of points for which the predicted label is equal to the true label (higher diagonal values are better since it indicates many correct predictions), off-diagonal elements are those mislabeled by the model (lower off-diagonal elements are better since it indicates lack of incorrect predictions)
9. **Convolutional Neural Network (CNN)**: Type of DNN specifically designed for image recognition and processing
10. **Epoch**: One complete iteration of the entire training dataset through the ML algorithm
11. **ESP32**: Series of low-cost, low-power system-on-chip microcontrollers with integrated WiFi and Bluetooth capabilities
12. **Espressif**: Manufacturer of ESP32 microcontrollers 
13. **Google Colab**: Hosted Jupyter Notebook service that requires no setup to use and provides both free and paid access to computing resources, including GPUs and TPUs
14. **Graphics Processing Unit (GPU)**: Specialized electronic circuit that can perform mathematical calculations at high speed; useful for training AI and DNNs
15. **Inference**: Process of using a trained ML model to make predictions, classifications, and/or detections on new data
16. **Local Access Network (LAN)**: Group of connected computing devices within a limited area (usually sharing a centralized Internet connection) that can communicate and share resources amongst each other
17. **Machine Learning (ML)**: Subfield of AI that involves training computer systems to learn from data and make decisions or predictions without being explicitly programmed
18. **Microcystis**: Very toxic genus of cyanobacteria which look like clusters of small dots and is known for forming harmful algal blooms in bodies of water
19. **Motion JPEG (MJPEG)**: Video compression format where each frame of a digital video sequence is compressed separately as a JPEG image
20. **Weights**: Numbers associated with the connections between neurons/nodes across different layers of a DNN
21. **Nitzschia**: Type of thin, elongated algae that can cause harmful algal blooms
22. **Normalize**: Within the context of confusion matrices, it means the matrix elements are displayed as a percentage
23. **Oscillatoria**: Genus of filamentous cyanobacteria that forms blue-green algal blooms
24. **PlatformIO**: Cross-platform, cross-architecture, multi-framework tool for embedded system engineers and software engineers who write embedded applications
25. **Python**: High-level programming language widely used for data analysis and ML
26. **PyTorch**: ML library used for various applications, including CV
27. **Red Tide**: Event which occurs on Florida’s coastline where algae grows uncontrollably
28. **Roboflow**: CV developer framework for better data collection, dataset preprocessing, dataset augmentation, model training techniques, model deployment, and more
29. **Slicing Aided Fine Tuning (SAFT)**: Novel approach that augments the fine-tuning dataset by dividing images into overlapping patches, thus providing a more balanced representation of small objects and overcoming the bias towards larger objects in the original pre-training datasets
30. **Slicing Aided Hyper Inference (SAHI)**: Common method of improving the detection accuracy of small objects, which involves running inference over portions of an image then accumulating the results
31. **Tensor Processing Unit (TPU)**: Google’s application-specific integrated circuit (ASIC) used to accelerate ML workloads; useful for training AI and DNNs
32. **Ultralytics**: Company that aims to make AI model development accessible, efficient to train, and easy to deploy
33. **Wireless Local Area Network (WLAN)**: Computer network that links two or more devices using wireless communication to form a LAN
34. **YOLOv8**: Version 8 of You Only Look Once, a high performance real-time object detection and image segmentation model developed by Ultralytics