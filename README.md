<div align="center">
<h1>Using AI and Low-Cost Camera to Detect Harmful Algae</h1>
<img alt="Python" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=Python+3.11.5&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1">
<img alt="C++" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=C%2B%2B&logo=c%2B%2B&color=00599c&labelColor=393939&logoColor=00599c">
<img alt="Conda" src="https://img.shields.io/static/v1?label=Package+Manager&style=flat&message=Conda&logo=anaconda&color=44A833&labelColor=393939&logoColor=44A833">
<img alt="PyTorch" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=PyTorch&logo=pytorch&color=EE4C2C&labelColor=393939&logoColor=EE4C2C">
<img alt="Jupyter" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Jupyter&logo=jupyter&color=F37626&labelColor=393939&logoColor=F37626">
<img alt="Colab" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Colab&logo=google+colab&color=F9AB00&labelColor=393939&logoColor=F9AB00">
<img alt="OpenCV" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=OpenCV&logo=opencv&color=5C3EE8&labelColor=393939&logoColor=5C3EE8">
<img alt="Arduino" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Arduino&logo=arduino&color=00878F&labelColor=393939&logoColor=00878F">
<img alt="Espressif" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Espressif&logo=espressif&color=E7352C&labelColor=393939&logoColor=E7352C">
<img alt="PlatformIO" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=PlatformIO&logo=platformio&color=F5822A&labelColor=393939&logoColor=F5822A">
<img alt="Ultralytics YOLOv8" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Ultralytics+YOLOv8&color=042AFF&labelColor=393939&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAyIiBoZWlnaHQ9IjUxMiIgdmlld0JveD0iMCAwIDUwMiA1MTIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8xMF8xNjgpIj4KPHBhdGggZD0iTTExNy41MTkgMC4wMDE2NDAzMkM1Mi43MTgyIDAuMDAxNjQwMzIgMi4zNzcwMmUtMDUgNTIuNzQ0MiAyLjM3NzAyZS0wNSAxMTcuNTc0QzIuMzc3MDJlLTA1IDE4Mi4zOTkgNTIuNzE4MiAyMzUuMTQzIDExNy41MTkgMjM1LjE0M0MxODIuMzIxIDIzNS4xNDMgMjM1LjAzOSAxODIuMzk5IDIzNS4wMzkgMTE3LjU3NEMyMzUuMDM5IDUyLjc0NDIgMTgyLjMyMSAwLjAwMTY0MDMyIDExNy41MTkgMC4wMDE2NDAzMloiIGZpbGw9IiMwQjIzQTkiLz4KPHBhdGggZD0iTTI1MC40OCAzNjguMTYxQzIwOC4xNDggMzY4LjE2MSAxNjguMTQ5IDM1Ny40MzggMTMzLjAzNyAzMzguNjExVjM5MS45NTJDMTMzLjAzNyA0NTYuNjgxIDE4NC43IDUxMC4zODkgMjQ5LjM5OCA1MTEuMDE1QzMxNC43MyA1MTEuNjQ2IDM2OC4wNzkgNDU4LjY2MiAzNjguMDc5IDM5My40NTFWMzM4LjU2MUMzMzIuOTM0IDM1Ny40MzUgMjkyLjg3IDM2OC4xNjEgMjUwLjQ4IDM2OC4xNjFaIiBmaWxsPSIjMEIyM0E5Ii8+CjxwYXRoIGQ9Ik0yNjUuODU4IDExNy41ODdDMjY1LjczNiAxOTkuMzc1IDE5OS4zNjkgMjY1Ljc5NyAxMTcuMzI0IDI2NS45OTdDODUuNjc0NyAyNjYuMDc5IDU1Ljk3NTYgMjU2LjIyMiAzMS43NCAyMzkuMDE0Qzc0LjY5NTMgMzE1LjgzMyAxNTYuNjYxIDM2OC4yMTEgMjUwLjM4NCAzNjguMDI5QzM4Ni41MzIgMzY4LjEzNyA0OTguODc1IDI1Ny4yNDIgNTAxLjE0NCAxMjEuMjMyTDUwMC44MjIgMTIwLjk0MUM1MDAuOTU2IDExNy41NTIgNTAwLjc5IDEyMC4zMjggNTAwLjk1NiAxMTcuNTUyQzUwMS4wMjEgNTIuNjc2NyA0NDguMjIyIC0wLjI3MTUwMiAzODMuNjk3IC0wLjA0NTYzMDNDMzE4LjU1OCAwLjIxMTU5NyAyNjUuOTIzIDUyLjcxMSAyNjUuODU4IDExNy41ODdaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMTBfMTY4KSIvPgo8L2c+CjxkZWZzPgo8bGluZWFyR3JhZGllbnQgaWQ9InBhaW50MF9saW5lYXJfMTBfMTY4IiB4MT0iMTQyLjEzNyIgeTE9IjM2My44NyIgeDI9IjQzMy4xMjMiIHkyPSI0MS42NjY1IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CjxzdG9wIHN0b3AtY29sb3I9IiMwOURCRjAiLz4KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjMEIyM0E5Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTBfMTY4Ij4KPHJlY3Qgd2lkdGg9IjUwMiIgaGVpZ2h0PSI1MTIiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==">
<img alt="Roboflow" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Roboflow&color=6706CE&labelColor=393939&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI1LjMuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCA2MDAgNjAwIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA2MDAgNjAwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO2ZpbGw6IzY3MDZDRTt9Cgkuc3Qxe2ZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO2ZpbGw6I0ZGRkZGRjt9Cjwvc3R5bGU+CjxnPgoJPGNpcmNsZSBjbGFzcz0ic3QwIiBjeD0iMzAwIiBjeT0iMzAwIiByPSIzMDAiLz4KPC9nPgo8Zz4KCTxwYXRoIGNsYXNzPSJzdDEiIGQ9Ik0yNzkuMzQsMjY3LjY3YzI3LjctMjEuNTgsMTUuNTUtNTEuMTEtMzAuMjQtNDUuNGMtNTMuMDMsNi42LTEyMC42Miw1OC40NS0xMzcuNDYsMTIwLjcKCQljLTEuMzgsNS4wOS0yLjQ1LDEwLjI3LTMuMTksMTUuNWMtMC43Myw1LjE1LTEuMTIsMTAuMzUtMS4xNywxNS41NWMtMC4wNSw1LjE1LDAuMjUsMTAuMywwLjg5LDE1LjQKCQljMC42NCw1LjExLDEuNjQsMTAuMTcsMi45OCwxNS4xNGMxLjM2LDUuMDMsMy4wNiw5Ljk3LDUuMDksMTQuNzZjMi4wOSw0LjkyLDQuNTEsOS42OCw3LjI0LDE0LjI2YzIuODMsNC43Niw1Ljk4LDkuMzEsOS40LDEzLjY0CgkJYzExLjY3LDE0Ljc4LDI2LjY1LDI3LjE2LDQyLjYzLDM3LjAyYzMuNDYsMi4xNCw3LjE4LDQuMjEsMTEuMjUsNC40MWM1Ljk0LDAuMjgsMTAuNDQtNC40NCwxMC42OC0xMC4yMwoJCWMwLjA5LTIuMTgtMC40Ni00LjI0LTEuNDYtNmMtMTMuNDItMjMuNjctMjQuNTItNTguODEtMjIuMjQtODAuOTlDMTc5LjQzLDMzNi4yOSwyMzUuMjgsMzAxLjk4LDI3OS4zNCwyNjcuNjd6Ii8+Cgk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNNTAwLjI4LDM2My44NGMtMi45LTYuOTEtMTAuMTYtMTAuODEtMTcuNTEtMTAuMTVjLTUuMDIsMC40NS05LjE3LDMuMTMtMTIuNTUsNi42OAoJCWMtNS40OSw0Ljk3LTkuMzEsMTEuODktMTMuNDMsMTcuOTFjLTQuODYsNy4wOC05Ljk0LDE0LjAyLTE1LjQxLDIwLjYzYy0xMC44LDEzLjA0LTIzLjI0LDI0Ljc5LTM3Ljc2LDMzLjYxCgkJYy0yNC42MywxNC45NS00Ny4xNywyMi4xMi03NC4yNyw4LjMxYy0xOS44My0xNS44Ni0xMy4xMy0zNC42LDMuMjktNDkuODdjMjguMDgtMjYuMSw2MS45My00NC40Miw4OC41Mi03Mi40NAoJCWMyNS0yNi4zNCw0Ny4wNS01OS4xMSw1Mi4yNC05NS43OGMxLjQ2LTEwLjI3LDEuNDgtMjAuNzQtMC4xNy0zMWMtNy44LTQ4LjMxLTUxLjQ4LTc4Ljk3LTk1LjU5LTkyLjAxCgkJQzMyMS40Nyw4My4xMywyNTkuNiw4OCwyMDYuNDgsMTEyLjU2Yy0yMS44NiwxMC4xMS00Mi4yMywyMy42NS01OS45NCwzOS45OGMtNy44NSw3LjI0LTE1LjI0LDE1LjAxLTIyLjEsMjMuMgoJCWMtMTEuMSwxMy4yNy0yMy43MywyOC43Ny0yNS44OSw0Ni41N2MtMS4zMywxMC45OSw4LjU4LDE4LjU5LDE4Ljk5LDE3LjE4YzYuOTgtMC45NCwxMy4xNi01LjE1LDE4LjMtOS43NAoJCWM1Ljk3LTUuMzMsMTEuNDUtMTEuMjUsMTcuMjEtMTYuODJjMTcuMzgtMTYuODIsMzUuOTQtMzIuNDcsNTguMDEtNDIuNzljMjguMTEtMTMuMTUsNTkuNjEtMTkuNTUsOTAuNi0xNi4zMgoJCWMzMS40MywzLjI3LDY5LjY3LDE3LjQ0LDgxLjE1LDQ5Ljk4YzExLjk3LDMzLjk3LTEzLjczLDY3LjM2LTM3LjE4LDg5LjA2Yy0zOC4yOSwzNS40NC0xMTAuOTksNzEuNjMtMTAyLjk4LDEzNC4xOQoJCWM0LjI5LDMzLjUxLDI4LjQsNjIuMTksNTkuMjQsNzQuOTZjNTMuNjYsMjIuMjMsMTExLjc0LTQuODQsMTQ4Ljg5LTQ2LjE4YzEyLjQ2LTEzLjI0LDMwLjM4LTM1LjgyLDQ2LjY4LTY5LjQ2CgkJQzUwMC42MSwzNzkuODQsNTAzLjIzLDM3MC44Nyw1MDAuMjgsMzYzLjg0eiIvPgo8L2c+Cjwvc3ZnPg==">
<br>
<img alt="Last Commit" src="https://img.shields.io/github/last-commit/lynkos/algae-detection?style=flat&label=Last+Commit&labelColor=393939&color=be0000">
<img alt="Commit Activity" src="https://img.shields.io/github/commit-activity/t/lynkos/algae-detection?style=flat&label=Commit+Activity&labelColor=393939&color=b30086">
<img alt="Repo Size" src="https://img.shields.io/github/repo-size/lynkos/algae-detection?style=flat&label=Repo+Size&labelColor=393939&color=ff62b1">
</div>

## Overview
Quickly detect and classify different species of harmful algae within natural water samples under a microscope in real-time via a fine-tuned convolutional neural network and low-cost camera (or, if preferred, smartphone).

The system can be used to monitor water quality and as a preventative measure for harmful algal blooms.

It's designed to be user-friendly and cost-effective, making it ideal for both research and educational purposes.

<details open>
   <summary><b>Nikon microscope equipped with ESP32-CAM AI Thinker and illuminator</b></summary>
   <div align="center"><img alt="Nikon microscope equipped with ESP32-CAM AI Thinker and illuminator" src="src/assets/microscope.jpg"></div>
</details>

<details>
   <summary><b>Dataset Classes</b></summary>
   <table align="center" style="width: 100%; text-align: center;">
      <tr>
         <th style="text-align: center;">Name</th>
         <th style="text-align: center;" width="100%">Example</th>
      </tr>
      <tr>
         <td>Closterium</td>
         <td><img alt="Closterium" align="center" width="100%" src="src/assets/algae/closterium.jpg"></td>
      </tr>
      <tr>
         <td>Microcystis</td>
         <td><img alt="Microcystis" align="center" width="100%" src="src/assets/algae/microcystis.jpg"></td>
      </tr>
      <tr>
         <td>Nitzschia</td>
         <td><img alt="Nitzschia" align="center" width="100%" src="src/assets/algae/nitzschia.jpg"></td>
      </tr>
      <tr>
         <td>Oscillatoria</td>
         <td><img alt="Oscillatoria" align="center" width="100%" src="src/assets/algae/oscillatoria.jpg"></td>
      </tr>
      <tr>
         <td>Non-Algae</td>
         <td><img alt="Non-Algae" align="center" width="100%" src="src/assets/algae/non-algae.jpg"></td>
      </tr>
   </table>
</details>

<details>
  <summary><b>Repository Structure</b></summary>
<pre>
.
├── documentation/
│   ├── installation_guide.md
│   ├── test_algae.pdf
│   └── user_manual.md
├── posters/
│   ├── cristian.pdf
│   ├── justin.pdf
│   └── kiran.pdf
├── presentation_slides
├── src/
│   ├── assets/
│   │   ├── algae/
│   │   │   ├── closterium.jpg
│   │   │   ├── microcystis.jpg
│   │   │   ├── nitzschia.jpg
│   │   │   ├── non-algae.jpg
│   │   │   └── oscillatoria.jpg
│   │   ├── custom_yolov8x/
│   │   │   ├── F1_curve.png
│   │   │   ├── PR_curve.png
│   │   │   ├── P_curve.png
│   │   │   ├── R_curve.png
│   │   │   ├── confusion_matrix.png
│   │   │   ├── confusion_matrix_normalized.png
│   │   │   ├── labels.jpg
│   │   │   ├── labels_correlogram.jpg
│   │   │   ├── results.png
│   │   │   └── validation.png
│   │   ├── sahi_yolov8n/
│   │   │   ├── F1_curve.png
│   │   │   ├── PR_curve.png
│   │   │   ├── P_curve.png
│   │   │   ├── R_curve.png
│   │   │   ├── confusion_matrix.png
│   │   │   ├── confusion_matrix_normalized.png
│   │   │   ├── results.png
│   │   │   └── validation.png
│   │   ├── esp32cam_ai_thinker.jpg
│   │   ├── index.png
│   │   ├── microscope.jpg
│   │   └── stream_settings_ui.png
│   ├── detection/
│   │   ├── base.py
│   │   ├── esp32.py
│   │   └── other.py
│   ├── streaming/
│   │   ├── boards/
│   │   │   └── esp32cam_ai_thinker.json
│   │   ├── html/
│   │   │   ├── index.html
│   │   │   └── index.min.html
│   │   ├── include/
│   │   │   ├── format_duration.h
│   │   │   ├── format_number.h
│   │   │   ├── lookup_camera_effect.h
│   │   │   ├── lookup_camera_frame_size.h
│   │   │   ├── lookup_camera_gainceiling.h
│   │   │   ├── lookup_camera_wb_mode.h
│   │   │   └── settings.h
│   │   ├── lib/
│   │   │   └── rtsp_server/
│   │   │       ├── library.json
│   │   │       ├── rtsp_server.cpp
│   │   │       └── rtsp_server.h
│   │   ├── src/
│   │   │   └── main.cpp
│   │   ├── generate_html.ps1
│   │   ├── generate_html.sh
│   │   ├── minify.py
│   │   ├── platformio.ini
│   │   └── README.md
│   └── model_pipeline.ipynb
├── videos/
│   └── index.html
├── weights/
│   ├── yolov8n_sahi.pt.zip
│   └── custom_yolov8x.pt.zip
├── .gitattributes
├── .gitignore
├── environment.yml
└── README.md
</pre>
</details>

## Requirements
- [x] ESP32-CAM AI Thinker
- [x] Nikon microscope with 3D printed lens attachment and illuminator
- [x] USB-C cable
- [x] Dataset
- [x] [Visual Studio Code](https://code.visualstudio.com/download)
- [x] [PlatformIO plugin for Visual Studio Code](https://docs.platformio.org/en/stable/integration/ide/vscode.html)
- [x] [Roboflow account](https://roboflow.com)
- [x] [Google Colab account](https://colab.research.google.com)
- [x] [Anaconda](https://docs.continuum.io/free/anaconda/install) **OR** [Miniconda](https://docs.conda.io/projects/miniconda/en/latest)

> [!NOTE]
> If you have trouble deciding between Anaconda and Miniconda, please refer to the table below:
> <table>
> <thead>
> <tr>
> <th><center>Anaconda</center></th>
> <th><center>Miniconda</center></th>
> </tr>
> </thead>
> <tbody>
> <tr>
> <td>New to conda and/or Python</td>
> <td>Familiar with conda and/or Python</td>
> </tr>
> <tr>
> <td>Like the convenience of having Python and 1,500+ scientific packages automatically installed at once</td>
> <td>Want fast access to Python and the conda commands and plan to sort out the other programs later</td>
> </tr>
> <tr>
> <td>Have the time and space (a few minutes and 3 GB)</td>
> <td>Don't have the time or space to install 1,500+ packages</td>
> </tr>
> <tr>
> <td>Don't want to individually install each package</td>
> <td>Don't mind individually installing each package</td>
> </tr>
> </tbody>
> </table>

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
4. Clone `algae-detection`
   ```sh
   git clone https://github.com/lynkos/algae-detection.git && cd algae-detection
   ```
> [!WARNING]
> Due to the [large] size of the repo, you may get errors such as:
> 
> <pre>error: RPC failed; curl 56 Recv failure: Connection reset by peer error: 6022 bytes of body are still expected fetch-pack: unexpected disconnect while reading sideband packet fatal: early EOF fatal: fetch-pack: invalid index-pack output</pre>
>
> If this is the case, please download [Git LFS](https://git-lfs.com) and try cloning again. If you're still getting errors, consider [cloning via SSH](https://github.com/git-guides/git-clone#git-clone-with-ssh) (`git clone git@github.com:lynkos/algae-detection.git`) or [manually downloading the repo as a `.zip` file](https://github.com/lynkos/algae-detection/archive/refs/heads/main.zip) and decompressing it.
5. Create conda virtual environment from [`environment.yml`](environment.yml)
   ```
   conda env create -f environment.yml
   ```
6. Activate `algae_env`
   ```
   conda activate algae_env
   ```
7. Confirm that `algae_env` is active
     * If active, `algae_env` should be in parentheses () or brackets [] before your command prompt, e.g.
       ```
       (algae_env) $
       ```
     * If necessary, see which virtual environments are available and/or currently active (active environment denoted with asterisk (*))
       ```
       conda info --envs
       ```
       **OR**
       ```
       conda env list
       ```
8. Read the files in [`documentation`](documentation) for more details

## Usage
### Detect and Classify Algae
1. Open [`weights`](weights)
2. Choose the algae detection model you want to use
   * To use your own `.pt` model, add it to [`weights`](weights)
   * To use an existing model, decompress the `.zip` file to get the `.pt` model
      * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Nano with [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference): [`yolov8n_sahi.pt.zip`](weights/yolov8n_sahi.pt.zip)
      * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Extra-Large: [`custom_yolov8x.pt.zip`](weights/custom_yolov8x.pt.zip)
3. Open [`base.py`](src/detection/base.py)
4. Set [`MODEL_PATH`](src/detection/base.py#L24) to path of desired `.pt` model
5. Read the following depending on which camera you'll use
   * [ESP32](#esp32)
   * [Webcam and/or iPhone](#webcam-andor-iphone)

#### ESP32
1. Follow the steps in [this specific `README.md`](src/streaming/README.md) to set up ESP32
2. Open [`esp32.py`](src/detection/esp32.py) once finished
3. Set [`URL`](src/detection/esp32.py#L3) to ESP32's IP address
4. Run [`esp32.py`](src/detection/esp32.py)
   * POSIX
      ```
      $(which python) src/detection/esp32.py
      ```
   * Windows
      ```
      $(where python) src\detection\esp32.py
      ```

#### Webcam and/or iPhone
1. Open [`other.py`](src/detection/other.py)
2. Set [`CAMERA_TYPE`](src/detection/other.py#L3) to `0` to use webcam or `1` to use iPhone
3. Run [`other.py`](src/detection/other.py)
   * POSIX
      ```
      $(which python) src/detection/other.py
      ```
   * Windows
      ```
      $(where python) src\detection\other.py
      ```

### Training, Validating, and Testing Model
All algae detection models trained and tested for this project have been fine-tuned with:

1. Small dataset of images (~1000 total) manually taken with the modified microscope and ESP32-CAM AI Thinker
2. Pre-trained models, such as [YOLOv8](https://docs.ultralytics.com/models/yolov8), [RT-DETR](https://docs.ultralytics.com/models/rtdetr), and [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference)

Only the top 2 highest performing algae detection models have been kept.

#### Google Colab (Recommended)
1. Visit [this Google Colab notebook](https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ)
2. Make sure you have your [Roboflow API key](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key), else you'll have to manually upload your Roboflow dataset and won't be able to deploy your model after it's trained
3. Click the key button in the left panel to add your Roboflow API key
4. Input `ROBOFLOW_API_KEY` within **Name** column and paste your [Roboflow API key](https://docs.roboflow.com/api-reference/authentication#retrieve-an-api-key) within **Value** column
5. Toggle **Notebook access** on
6. Click **Add new secret**
7. Run notebook

#### [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
1. Open the Command Palette in Visual Studio Code with the relevant keyboard shortcut
    * Mac
      ```
      ⌘ + Shift + P
      ```
    * PC
      ```
      CTRL + Shift + P
      ```
2. Search and select `Python: Select Interpreter`
3. Select `algae_env`
4. Open [`model-pipeline.ipynb`](src/model_pipeline.ipynb)
5. Confirm `algae_env` is the selected [kernel](https://docs.jupyter.org/en/latest/install/kernels.html)
6. Run [`model-pipeline.ipynb`](src/model_pipeline.ipynb): Click `Run All`
7. Deactivate `algae_env` once finished
   ```
   conda deactivate
   ```

## Future Work
- [ ] Increase dataset and improve model accuracy and versatility by taking quality images of various types of algae
   - At least [1000 images per class](https://blog.roboflow.com/model-best-practices/#dataset-size) 
   - [All classes are balanced](https://blog.roboflow.com/handling-unbalanced-classes) (i.e., have roughly the same amount of images)
   - [Dr. Schonna R. Manning](https://case.fiu.edu/about/directory/profiles/manning-schonna-r..html) may help with categorizing any algae in new images
   - Further reading: [1](https://www.usgs.gov/news/national-news-release/usgs-finds-28-types-cyanobacteria-florida-algal-bloom), [2](https://myfwc.com/research/wildlife/health/cyanobacteria/#:~:text=Approximately%2020%20cyanobacteria%20species%20in,than%20one%20type%20of%20toxin), [3](https://pubs.usgs.gov/publication/ofr20171054), and/or research "[toxic cyanobacteria](https://www.google.com/search?q=toxic+cyanobacteria)"
- [ ] Connect to ESP32 without a web server (e.g., via USB, etc.), just like Webcam and iPhone OR use RTSP instead of HTTP
- [ ] Heatsink for ESP32 to prevent overheating
- [ ] Run model on ESP32 rather than on computer
- [ ] Update microscope's 3D printed lens attachment by making it adjustable OR create multiple ones for different devices, e.g., Phone, Android, etc.
- [ ] Add Android compatability (assuming it isn't)

## Credits
Special thanks to:
- [Dr. Antao Chen](https://ieeexplore.ieee.org/author/37291140300) (product owner) for his mentorship
- [rzeldent](https://github.com/rzeldent) for [ESP32CAM-RTSP](https://github.com/rzeldent/esp32cam-rtsp/tree/develop), which has been modified and used in [`streaming`](src/streaming)
- [rdgbrian](https://github.com/rdgbrian) (last semester's team lead) for his assistance
