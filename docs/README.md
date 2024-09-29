<div align="center">
<h1>Using AI and Low-Cost Camera to Detect Harmful Algae</h1>
<img alt="Python" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=Python+3.11.5&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1">
<img alt="C++" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=C%2B%2B&logo=c%2B%2B&color=00599c&labelColor=393939&logoColor=00599c">
<img alt="HTML" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=HTML&logo=HTML5&color=E34F26&labelColor=393939&logoColor=E34F26">
<img alt="Shell" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=Shell&logo=GNU+Bash&color=4EAA25&labelColor=393939&logoColor=4EAA25">
<img alt="C" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=C&logo=C&color=a8b9cc&labelColor=393939&logoColor=a8b9cc">
<br>
<img alt="Ultralytics YOLOv8" src="https://img.shields.io/static/v1?label=Frameworks&style=flat&message=Ultralytics+YOLOv8&color=042AFF&labelColor=393939&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAyIiBoZWlnaHQ9IjUxMiIgdmlld0JveD0iMCAwIDUwMiA1MTIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8xMF8xNjgpIj4KPHBhdGggZD0iTTExNy41MTkgMC4wMDE2NDAzMkM1Mi43MTgyIDAuMDAxNjQwMzIgMi4zNzcwMmUtMDUgNTIuNzQ0MiAyLjM3NzAyZS0wNSAxMTcuNTc0QzIuMzc3MDJlLTA1IDE4Mi4zOTkgNTIuNzE4MiAyMzUuMTQzIDExNy41MTkgMjM1LjE0M0MxODIuMzIxIDIzNS4xNDMgMjM1LjAzOSAxODIuMzk5IDIzNS4wMzkgMTE3LjU3NEMyMzUuMDM5IDUyLjc0NDIgMTgyLjMyMSAwLjAwMTY0MDMyIDExNy41MTkgMC4wMDE2NDAzMloiIGZpbGw9IiMwQjIzQTkiLz4KPHBhdGggZD0iTTI1MC40OCAzNjguMTYxQzIwOC4xNDggMzY4LjE2MSAxNjguMTQ5IDM1Ny40MzggMTMzLjAzNyAzMzguNjExVjM5MS45NTJDMTMzLjAzNyA0NTYuNjgxIDE4NC43IDUxMC4zODkgMjQ5LjM5OCA1MTEuMDE1QzMxNC43MyA1MTEuNjQ2IDM2OC4wNzkgNDU4LjY2MiAzNjguMDc5IDM5My40NTFWMzM4LjU2MUMzMzIuOTM0IDM1Ny40MzUgMjkyLjg3IDM2OC4xNjEgMjUwLjQ4IDM2OC4xNjFaIiBmaWxsPSIjMEIyM0E5Ii8+CjxwYXRoIGQ9Ik0yNjUuODU4IDExNy41ODdDMjY1LjczNiAxOTkuMzc1IDE5OS4zNjkgMjY1Ljc5NyAxMTcuMzI0IDI2NS45OTdDODUuNjc0NyAyNjYuMDc5IDU1Ljk3NTYgMjU2LjIyMiAzMS43NCAyMzkuMDE0Qzc0LjY5NTMgMzE1LjgzMyAxNTYuNjYxIDM2OC4yMTEgMjUwLjM4NCAzNjguMDI5QzM4Ni41MzIgMzY4LjEzNyA0OTguODc1IDI1Ny4yNDIgNTAxLjE0NCAxMjEuMjMyTDUwMC44MjIgMTIwLjk0MUM1MDAuOTU2IDExNy41NTIgNTAwLjc5IDEyMC4zMjggNTAwLjk1NiAxMTcuNTUyQzUwMS4wMjEgNTIuNjc2NyA0NDguMjIyIC0wLjI3MTUwMiAzODMuNjk3IC0wLjA0NTYzMDNDMzE4LjU1OCAwLjIxMTU5NyAyNjUuOTIzIDUyLjcxMSAyNjUuODU4IDExNy41ODdaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMTBfMTY4KSIvPgo8L2c+CjxkZWZzPgo8bGluZWFyR3JhZGllbnQgaWQ9InBhaW50MF9saW5lYXJfMTBfMTY4IiB4MT0iMTQyLjEzNyIgeTE9IjM2My44NyIgeDI9IjQzMy4xMjMiIHkyPSI0MS42NjY1IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CjxzdG9wIHN0b3AtY29sb3I9IiMwOURCRjAiLz4KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjMEIyM0E5Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTBfMTY4Ij4KPHJlY3Qgd2lkdGg9IjUwMiIgaGVpZ2h0PSI1MTIiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==">
<img alt="OpenCV" src="https://img.shields.io/static/v1?label=Frameworks&style=flat&message=OpenCV&logo=opencv&color=5C3EE8&labelColor=393939&logoColor=5C3EE8">
<img alt="Roboflow" src="https://img.shields.io/static/v1?label=Frameworks&style=flat&message=Roboflow&color=6706CE&labelColor=393939&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI1LjMuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCA2MDAgNjAwIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA2MDAgNjAwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO2ZpbGw6IzY3MDZDRTt9Cgkuc3Qxe2ZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO2ZpbGw6I0ZGRkZGRjt9Cjwvc3R5bGU+CjxnPgoJPGNpcmNsZSBjbGFzcz0ic3QwIiBjeD0iMzAwIiBjeT0iMzAwIiByPSIzMDAiLz4KPC9nPgo8Zz4KCTxwYXRoIGNsYXNzPSJzdDEiIGQ9Ik0yNzkuMzQsMjY3LjY3YzI3LjctMjEuNTgsMTUuNTUtNTEuMTEtMzAuMjQtNDUuNGMtNTMuMDMsNi42LTEyMC42Miw1OC40NS0xMzcuNDYsMTIwLjcKCQljLTEuMzgsNS4wOS0yLjQ1LDEwLjI3LTMuMTksMTUuNWMtMC43Myw1LjE1LTEuMTIsMTAuMzUtMS4xNywxNS41NWMtMC4wNSw1LjE1LDAuMjUsMTAuMywwLjg5LDE1LjQKCQljMC42NCw1LjExLDEuNjQsMTAuMTcsMi45OCwxNS4xNGMxLjM2LDUuMDMsMy4wNiw5Ljk3LDUuMDksMTQuNzZjMi4wOSw0LjkyLDQuNTEsOS42OCw3LjI0LDE0LjI2YzIuODMsNC43Niw1Ljk4LDkuMzEsOS40LDEzLjY0CgkJYzExLjY3LDE0Ljc4LDI2LjY1LDI3LjE2LDQyLjYzLDM3LjAyYzMuNDYsMi4xNCw3LjE4LDQuMjEsMTEuMjUsNC40MWM1Ljk0LDAuMjgsMTAuNDQtNC40NCwxMC42OC0xMC4yMwoJCWMwLjA5LTIuMTgtMC40Ni00LjI0LTEuNDYtNmMtMTMuNDItMjMuNjctMjQuNTItNTguODEtMjIuMjQtODAuOTlDMTc5LjQzLDMzNi4yOSwyMzUuMjgsMzAxLjk4LDI3OS4zNCwyNjcuNjd6Ii8+Cgk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNNTAwLjI4LDM2My44NGMtMi45LTYuOTEtMTAuMTYtMTAuODEtMTcuNTEtMTAuMTVjLTUuMDIsMC40NS05LjE3LDMuMTMtMTIuNTUsNi42OAoJCWMtNS40OSw0Ljk3LTkuMzEsMTEuODktMTMuNDMsMTcuOTFjLTQuODYsNy4wOC05Ljk0LDE0LjAyLTE1LjQxLDIwLjYzYy0xMC44LDEzLjA0LTIzLjI0LDI0Ljc5LTM3Ljc2LDMzLjYxCgkJYy0yNC42MywxNC45NS00Ny4xNywyMi4xMi03NC4yNyw4LjMxYy0xOS44My0xNS44Ni0xMy4xMy0zNC42LDMuMjktNDkuODdjMjguMDgtMjYuMSw2MS45My00NC40Miw4OC41Mi03Mi40NAoJCWMyNS0yNi4zNCw0Ny4wNS01OS4xMSw1Mi4yNC05NS43OGMxLjQ2LTEwLjI3LDEuNDgtMjAuNzQtMC4xNy0zMWMtNy44LTQ4LjMxLTUxLjQ4LTc4Ljk3LTk1LjU5LTkyLjAxCgkJQzMyMS40Nyw4My4xMywyNTkuNiw4OCwyMDYuNDgsMTEyLjU2Yy0yMS44NiwxMC4xMS00Mi4yMywyMy42NS01OS45NCwzOS45OGMtNy44NSw3LjI0LTE1LjI0LDE1LjAxLTIyLjEsMjMuMgoJCWMtMTEuMSwxMy4yNy0yMy43MywyOC43Ny0yNS44OSw0Ni41N2MtMS4zMywxMC45OSw4LjU4LDE4LjU5LDE4Ljk5LDE3LjE4YzYuOTgtMC45NCwxMy4xNi01LjE1LDE4LjMtOS43NAoJCWM1Ljk3LTUuMzMsMTEuNDUtMTEuMjUsMTcuMjEtMTYuODJjMTcuMzgtMTYuODIsMzUuOTQtMzIuNDcsNTguMDEtNDIuNzljMjguMTEtMTMuMTUsNTkuNjEtMTkuNTUsOTAuNi0xNi4zMgoJCWMzMS40MywzLjI3LDY5LjY3LDE3LjQ0LDgxLjE1LDQ5Ljk4YzExLjk3LDMzLjk3LTEzLjczLDY3LjM2LTM3LjE4LDg5LjA2Yy0zOC4yOSwzNS40NC0xMTAuOTksNzEuNjMtMTAyLjk4LDEzNC4xOQoJCWM0LjI5LDMzLjUxLDI4LjQsNjIuMTksNTkuMjQsNzQuOTZjNTMuNjYsMjIuMjMsMTExLjc0LTQuODQsMTQ4Ljg5LTQ2LjE4YzEyLjQ2LTEzLjI0LDMwLjM4LTM1LjgyLDQ2LjY4LTY5LjQ2CgkJQzUwMC42MSwzNzkuODQsNTAzLjIzLDM3MC44Nyw1MDAuMjgsMzYzLjg0eiIvPgo8L2c+Cjwvc3ZnPg==">
<img alt="PyTorch" src="https://img.shields.io/static/v1?label=Frameworks&style=flat&message=PyTorch&logo=pytorch&color=EE4C2C&labelColor=393939&logoColor=EE4C2C">
<img alt="Espressif" src="https://img.shields.io/static/v1?label=Frameworks&style=flat&message=Espressif&logo=espressif&color=E7352C&labelColor=393939&logoColor=E7352C">
<img alt="Arduino" src="https://img.shields.io/static/v1?label=Frameworks&style=flat&message=Arduino&logo=arduino&color=00878F&labelColor=393939&logoColor=00878F">
<br>
<img alt="Conda" src="https://img.shields.io/static/v1?label=Tools&style=flat&message=Conda&logo=anaconda&color=44A833&labelColor=393939&logoColor=44A833">
<img alt="PlatformIO" src="https://img.shields.io/static/v1?label=Tools&style=flat&message=PlatformIO&logo=platformio&color=F5822A&labelColor=393939&logoColor=F5822A">
<img alt="Colab" src="https://img.shields.io/static/v1?label=Tools&style=flat&message=Colab&logo=google+colab&color=F9AB00&labelColor=393939&logoColor=F9AB00">
<br><br>
<a target="_blank" href="https://universe.roboflow.com/capstone2algae/algae-detection-1opyx/model"><img width="auto" height="25px" alt="Try YOLOv8 model on Roboflow" src="https://app.roboflow.com/images/try-model-badge.svg"/></a>
<a target="_blank" href="https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ"><img width="150px" height="auto" alt="Open in Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>
</div>

## Overview
This project aims to provide a practical, convenient, and efficient tool to monitor water quality and mitigate / prevent harmful algal blooms in real-time by:
- [x] Fine-tuning pre-trained AI models to detect harmful algae
- [x] Leveraging the portability of smartphones and low-cost cameras
   - Tested with [ESP32-CAM AI Thinker](https://docs.ai-thinker.com/en/esp32-cam) and [ESP32-S3-EYE](https://www.espressif.com/en/products/devkits/esp-eye/overview), but compatible with a large variety of other boards/SoCs
   - See '[Boards](appendix.md#boards)' section in [`appendix.md`](appendix.md) for full list of compatible cameras

Since it's designed to be user-friendly and cost-effective, it's also suitable for educational and research purposes.

<details open>
   <summary>Project Demo</summary>

   <div align="center">
      <figure>
         <picture><img alt="Program demo" src="../assets/misc/demo.gif"></picture><br>
         <figcaption style="font-size: 11px;">Detected algae are annotated with a bounding box, predicted class/category, and the AI model's confidence in its prediction(s). Trackbars allow user to configure the AI model's attributes — Confidence, IoU (i.e., Intersection over Union), and Max Detections — in real time.</figcaption>
      </figure>
   </div>
</details>

<details open>
   <summary><a href="../weights/custom_yolov8n.pt"><code>custom_yolov8n.pt</code></a> (i.e., custom AI model) validation results</summary>
   
   <div align="center">
      <table style="width: 100%; text-align: center;">
         <tr>
            <th style="text-align: center;">Predict</th>
            <th style="text-align: center;">Correct</th>
        </tr>
        <tr>
            <td><img alt="custom_yolov8n's inference results" align="center" src="../assets/models/custom_yolov8n/val_pred.jpg"></td>
            <td><img alt="Actual labels" align="center" src="../assets/models/custom_yolov8n/val_label.jpg"></td>
        </tr>
    </table>
   <p style="font-size: 11px;">Though it may appear so, these aren't duplicates! The left image shows what the model detected, while the right image shows the correct labels. The original images are from one of the batches in the model's validation dataset.</p>
   </div>
</details>

<details open>
   <summary>Hardware: Nikon microscope with ESP32-CAM AI Thinker and illuminator</summary>

   <div align="center">
      <figure>
         <picture><img alt="Nikon microscope equipped with ESP32-CAM AI Thinker and illuminator" src="../assets/misc/microscope.jpg"></picture><br>
         <figcaption style="font-size: 11px;">ESP32-CAM AI Thinker inside a custom 3D printed lens attachment atop the microscope's eyepiece.</figcaption>
      </figure>
   </div>
</details>

## Requirements
> [!IMPORTANT]
> <a target="_blank" href="https://docs.conda.io/en/latest">Conda</a> is technically the only hard requirement, though by itself provides a barebones experience and doesn't show the program's full functionality.
> 
> Refer to [Customization](appendix.md#customization) in [`appendix.md`](appendix.md) if you don't want to or can't use a(n) ESP32-CAM and/or microscope.

- [ ] Any of the [boards](appendix.md#boards) listed in [`appendix.md`](appendix.md)
- [ ] Nikon microscope with 3D printed lens attachment and illuminator
- [ ] Micro-USB cable (to connect board to computer)
- [ ] <a target="_blank" href="https://roboflow.com">Roboflow account</a>
- [ ] Dataset
   * <a target="_blank" href="https://drive.google.com/drive/folders/1gd85o6dpcjDwWJUUi4x9slhjHHuoY4K0">Google Drive</a>: Original and unedited
   * <a target="_blank" href="https://universe.roboflow.com/capstone2algae/algae-detection-1opyx/dataset">Roboflow</a>: Includes annotations, pre-processing, and augmentation
- [ ] <a target="_blank" href="https://code.visualstudio.com/download">Visual Studio Code</a>
- [ ] <a target="_blank" href="https://platformio.org/install/ide?install=vscode">PlatformIO plugin for Visual Studio Code</a>
- [ ] <a target="_blank" href="https://accounts.google.com/ServiceLogin?passive=true&continue=https%3A%2F%2Fcolab.research.google.com">Google Colab account</a>
- [x] <a target="_blank" href="https://docs.continuum.io/free/anaconda/install">Anaconda</a> **OR** <a target="_blank" href="https://docs.conda.io/projects/miniconda/en/latest">Miniconda</a>

> [!TIP]
> If you have trouble deciding between Anaconda and Miniconda, please refer to the table below:
> <table>
>  <thead>
>   <tr>
>    <th><center>Anaconda</center></th>
>    <th><center>Miniconda</center></th>
>   </tr>
>  </thead>
>  <tbody>
>   <tr>
>    <td>New to conda and/or Python</td>
>    <td>Familiar with conda and/or Python</td>
>   </tr>
>   <tr>
>    <td>Not familiar with using terminal and prefer GUI</td>
>    <td>Comfortable using terminal</td>
>   </tr>
>   <tr>
>    <td>Like the convenience of having Python and 1,500+ scientific packages automatically installed at once</td>
>    <td>Want fast access to Python and the conda commands and plan to sort out the other programs later</td>
>   </tr>
>   <tr>
>    <td>Have the time and space (a few minutes and 3 GB)</td>
>    <td>Don't have the time or space to install 1,500+ packages</td>
>   </tr>
>   <tr>
>    <td>Don't want to individually install each package</td>
>    <td>Don't mind individually installing each package</td>
>   </tr>
>  </tbody>
> </table>
>
> Typing out entire Conda commands can sometimes be tedious, so I wrote a shell script ([`conda_shortcuts.sh` on GitHub Gist](https://gist.github.com/lynkos/7a4ce7f9e38bb56174360648461a3dc8)) to define shortcuts for commonly used Conda commands.
> <details>
>   <summary>Example: Delete/remove a conda environment named <code>test_env</code></summary>
>
> * Shortcut command
>     ```
>     rmenv test_env
>     ```
> * Manually typing out the entire command
>     ```sh
>     conda env remove -n test_env && rm -rf $(conda info --base)/envs/test_env
>     ```
>
> The shortcut has 80.8% fewer characters!
> </details>

## Installation
1. Verify that conda is installed
   ```
   conda --version
   ```

2. Ensure conda is up to date
   ```
   conda update conda
   ```

3. Enter the directory you want `algae-detection` to be cloned in
   * POSIX
      ```sh
      cd ~/path/to/directory
      ```
   * Windows
      ```sh
      cd C:\Users\user\path\to\directory
      ```

4. Clone and enter `algae-detection`
   ```sh
   git clone https://github.com/lynkos/algae-detection.git && cd algae-detection
   ```

5. Create virtual environment from [`environment.yml`](../environment.yml)
   ```sh
   conda env create -f environment.yml
   ```

## Quick Start
<ol>
   <li>Activate <code>algae_env</code> (i.e., virtual environment)<pre>conda activate algae_env</pre></li>
   <li>Confirm <code>algae_env</code> is active
      <ul>
        <li><code>algae_env</code> should be in parentheses () or brackets [] before your command prompt, e.g.<pre>(algae_env) $</pre></li>
        <li>See which virtual environments are available and/or currently active (active environment denoted with asterisk (*))<pre>conda info --envs</pre> <b>OR</b> <pre>conda env list</pre></li>
      </ul>
   </li>
   <li id="s3">Run <a href="../src/detection/camera.py"><code>camera.py</code></a></li>
</ol>

> [!IMPORTANT]
> Automatically uses computer's default camera (i.e., webcam). To use different cameras:
> 
> * **ESP32-CAM**
>    * Refer to [ESP32-CAM tutorial](manual.md#esp32-cam) in [`manual.md`](manual.md)
> * **iPhone**
>     * Requires macOS v13+ and iOS v16+ (see [Apple's user guide](https://support.apple.com/guide/mac-help/use-iphone-as-a-webcam-mchl77879b8a/mac) for further details)
>     * Connect iPhone to Mac via USB before following [Step #3](#s3)
>     * Run [`camera.py`](../src/detection/camera.py) with argument `--cam 1`
>     * <details><summary>Connected iPhone</summary><div align="center"><img alt="iPhone connected" src="../assets/misc/iphone_ui_connect.png"></div></details>
> 
> <details>
>   <summary>User Interface</summary>
>
>   <div align="center">
>    <figure>
>    <picture><img alt="User Interface" src="../assets/misc/user_interface.png"></picture><br>
>    <figcaption style="font-size: 11px;">Users can view live footage from the camera. Detected algae are annotated with a bounding box, predicted class/category, and the model's confidence. Trackbars allow user to configure detection model attributes in real time.</figcaption>
>    </figure>
>   </div>
> </details>
>
> See [Command Line Arguments table](manual.md#command-line-arguments) in [`manual.md`](manual.md) for all possible arguments!

   <ul>
      <li>POSIX<br><pre>python src/detection/camera.py</pre></li>
      <li>Windows<br><pre>python src\detection\camera.py</pre></li>
   </ul>
</p>

<ol start="4">
   <li>Press the 'Escape' key on your keyboard to terminate</li>
</ol>

## Additional Information
- <a target="_blank" href="https://github.com/rzeldent/esp32cam-rtsp/tree/develop">ESP32CAM-RTSP</a> ([credit: rzeldent](#credits))

### [Appendix](appendix.md)
- [Boards](appendix.md#boards)
- [Diagrams](appendix.md#diagrams)
- [Customization](appendix.md#customization)
  - [Custom Dataset](appendix.md#custom-dataset)
  - [ESP32-CAM](appendix.md#esp32-cam)
- [Inference Deployed Model](appendix.md#inference-deployed-model)
- [Future Work](appendix.md#future-work)
- [Further Reading](appendix.md#further-reading)
- [Glossary](appendix.md#glossary)

### [Manual](manual.md)
- [Command Line Arguments](manual.md#command-line-arguments)
- [ESP32-CAM](manual.md#esp32-cam)
  - [Initial Setup](manual.md#initial-setup)
  - [Usage](manual.md#usage)
- [Train, Validate, and Test Model](manual.md#train-validate-and-test-model)
- [Select Model](manual.md#select-model)
  
## Credits
Special thanks to:
- <a target="_blank" href="https://ieeexplore.ieee.org/author/37291140300">Dr. Antao Chen</a> (product owner) for his mentorship
- <a target="_blank" href="https://github.com/rdgbrian">rdgbrian</a> (Fall 2023 team lead) for his assistance
- <a target="_blank" href="https://github.com/rzeldent">rzeldent</a> for <a target="_blank" href="https://github.com/rzeldent/esp32cam-rtsp/tree/develop">ESP32CAM-RTSP</a>, which has been slightly modified and added as a git subtree in [`streaming`](../src/streaming)
