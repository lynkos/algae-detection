<div align="center">
<h1>Using AI and Low-Cost Camera to Detect Harmful Algae</h1>
<img alt="Python" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=Python+3.11.5&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1">
<img alt="C++" src="https://img.shields.io/static/v1?label=Languages&style=flat&message=C%2B%2B&logo=c%2B%2B&color=00599c&labelColor=393939&logoColor=00599c">
<img alt="Conda" src="https://img.shields.io/static/v1?label=Package+Manager&style=flat&message=Conda&logo=anaconda&color=44A833&labelColor=393939&logoColor=44A833"><br>
<img alt="PyTorch" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=PyTorch&logo=pytorch&color=EE4C2C&labelColor=393939&logoColor=EE4C2C">
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
   <summary><b>Nikon microscope with ESP32-CAM AI Thinker and illuminator</b></summary>
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
   <summary><b>Diagrams</b></summary>
      <div align="center">
         <figure>
            <picture><img alt="ESP32-CAM system design" src="src/assets/diagrams/esp32_sys_des.png"></picture><br>
            <figcaption>System Design (ESP32-CAM)</figcaption>
         </figure><br><br>
         <figure>
            <picture><img alt="iPhone system design" src="src/assets/diagrams/iphone_sys_des.png"></picture><br>
            <figcaption>System Design (iPhone)</figcaption>
         </figure><br><br>
         <figure>
            <picture><img alt="Dataset flowchart" src="src/assets/diagrams/dataset_flowchart.png"></picture><br>
            <figcaption>Dataset Flowchart</figcaption>
         </figure><br><br>
         <figure>
            <picture><img alt="YOLOv8 architecture" src="src/assets/diagrams/yolov8_architecture.jpg"></picture><br>
            <figcaption><a target="_blank" href="https://mmyolo.readthedocs.io/en/latest/recommended_topics/algorithm_descriptions/yolov8_description.html">YOLOv8 Architecture</a></figcaption>
         </figure><br><br>
         <figure>
            <picture><img alt="Slicing Aided Fine Tuning (SAFT) framework" src="src/assets/diagrams/saft_framework.png"></picture><br>
            <figcaption><a href="https://arxiv.org/abs/2202.06934" target="_blank">Slicing Aided Fine Tuning (SAFT) Framework</a></figcaption>
         </figure><br><br>
         <figure>
            <picture><img alt="Slicing Aided Hyper Inference (SAHI) framework" src="src/assets/diagrams/sahi_framework.png"></picture><br>
            <figcaption><a href="https://arxiv.org/abs/2202.06934" target="_blank">Slicing Aided Hyper Inference (SAHI) Framework</a></figcaption>
         </figure>
      </div>
</details>

<details>
   <summary><b>Models' Performance</b></summary>
   <table align="center" style="width: 100%; text-align: center; display: block; max-width: -moz-fit-content; max-width: fit-content; margin: 0 auto; overflow-x: auto; white-space: nowrap;">
      <tr>
         <th style="text-align: center;">[Pre-Trained] Model</th>
         <th style="text-align: center;">Confusion Matrix (Normalized)</th>
         <th style="text-align: center;">Precision-Confidence Curve</th>
         <th style="text-align: center;">Precision-Recall Curve</th>
         <th style="text-align: center;">Recall-Confidence Curve</th>
         <th style="text-align: center;">F1-Confidence Curve</th>
         <th style="text-align: center;">Training Results</th>
         <th style="text-align: center;">Validation Output</th>
         <th style="text-align: center;">Example Prediction</th>
      </tr>
      <tr>
         <td><a href="https://docs.ultralytics.com/models/yolov8">YOLOv8</a> Extra-Large</td>
         <td><img alt="Confusion Matrix (Normalized)" align="center" src="src/assets/models/custom_yolov8x/confusion_matrix_normalized.png"></td>
         <td><img alt="Precision-Confidence Curve" align="center" src="src/assets/models/custom_yolov8x/P_curve.png"></td>
         <td><img alt="Precision-Recall Curve" align="center" src="src/assets/models/custom_yolov8x/PR_curve.png"></td>
         <td><img alt="Recall-Confidence Curve" align="center" src="src/assets/models/custom_yolov8x/R_curve.png"></td>
         <td><img alt="F1-Confidence Curve" align="center" src="src/assets/models/custom_yolov8x/F1_curve.png"></td>
         <td><img alt="Training Results" align="center" src="src/assets/models/custom_yolov8x/results.png"></td>
         <td><img alt="Validation Output" align="center" src="src/assets/models/custom_yolov8x/validation.png"></td>
         <td><img alt="Example Prediction" align="center" src="src/assets/models/custom_yolov8x/example.jpg"></td>
      </tr>
      <tr>
         <td><a href="https://docs.ultralytics.com/models/yolov8">YOLOv8</a> Extra-Large v2</td>
         <td><img alt="Confusion Matrix (Normalized)" align="center" src="src/assets/models/custom_yolov8x_v2/confusion_matrix_normalized.png"></td>
         <td><img alt="Precision-Confidence Curve" align="center" src="src/assets/models/custom_yolov8x_v2/P_curve.png"></td>
         <td><img alt="Precision-Recall Curve" align="center" src="src/assets/models/custom_yolov8x_v2/PR_curve.png"></td>
         <td><img alt="Recall-Confidence Curve" align="center" src="src/assets/models/custom_yolov8x_v2/R_curve.png"></td>
         <td><img alt="F1-Confidence Curve" align="center" src="src/assets/models/custom_yolov8x_v2/F1_curve.png"></td>
         <td><img alt="Training Results" align="center" src="src/assets/models/custom_yolov8x_v2/results.png"></td>
         <td><img alt="Validation Output" align="center" src="src/assets/models/custom_yolov8x_v2/validation.png"></td>
         <td><img alt="Example Prediction" align="center" src="src/assets/models/custom_yolov8x_v2/example.png"></td>
      </tr>
      <tr>
         <td><a href="https://docs.ultralytics.com/models/yolov8">YOLOv8</a> Nano with <a href="https://docs.ultralytics.com/guides/sahi-tiled-inference">SAHI</a></td>
         <td><img alt="Confusion Matrix (Normalized)" align="center" src="src/assets/models/sahi_yolov8n/confusion_matrix_normalized.png"></td>
         <td><img alt="Precision-Confidence Curve" align="center" src="src/assets/models/sahi_yolov8n/P_curve.png"></td>
         <td><img alt="Precision-Recall Curve" align="center" src="src/assets/models/sahi_yolov8n/PR_curve.png"></td>
         <td><img alt="Recall-Confidence Curve" align="center" src="src/assets/models/sahi_yolov8n/R_curve.png"></td>
         <td><img alt="F1-Confidence Curve" align="center" src="src/assets/models/sahi_yolov8n/F1_curve.png"></td>
         <td><img alt="Training Results" align="center" src="src/assets/models/sahi_yolov8n/results.png"></td>
         <td><img alt="Validation Output" align="center" src="src/assets/models/sahi_yolov8n/validation.png"></td>
         <td><img alt="Example Prediction" align="center" src="src/assets/models/sahi_yolov8n/example.jpg"></td>
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
├── presentation_slides/
│   └── algae_detection_ppt.pdf
├── src/
│   ├── assets/
│   │   ├── algae/
│   │   │   ├── closterium.jpg
│   │   │   ├── microcystis.jpg
│   │   │   ├── nitzschia.jpg
│   │   │   ├── non-algae.jpg
│   │   │   └── oscillatoria.jpg
│   │   ├── diagrams/
│   │   │   ├── dataset_flowchart.png
│   │   │   ├── esp32_sys_des.png
│   │   │   ├── iphone_sys_des.png
│   │   │   ├── saft_framework.png
│   │   │   ├── sahi_framework.png
│   │   │   └── yolov8_architecture.jpg
│   │   ├── esp32/
│   │   │   ├── ai_thinker.jpg
│   │   │   ├── ap_popup.png
│   │   │   ├── build_upload_monitor.png
│   │   │   ├── choose_ap.png
│   │   │   ├── config.png
│   │   │   ├── disconnect.png
│   │   │   ├── esp32_ip.png
│   │   │   ├── index.png
│   │   │   ├── init_config.png
│   │   │   ├── open_streaming.png
│   │   │   └── platformio_folder.png
│   │   ├── iphone/
│   │   │   ├── iphone_ui_connect.png
│   │   │   └── iphone_ui_disconnect.png
│   │   ├── models/
│   │   │   ├── custom_yolov8x/
│   │   │   │   ├── confusion_matrix_normalized.png
│   │   │   │   ├── confusion_matrix.png
│   │   │   │   ├── example.jpg
│   │   │   │   ├── F1_curve.png
│   │   │   │   ├── P_curve.png
│   │   │   │   ├── PR_curve.png
│   │   │   │   ├── R_curve.png
│   │   │   │   ├── results.png
│   │   │   │   └── validation.png
│   │   │   ├── custom_yolov8x_v2/
│   │   │   │   ├── confusion_matrix_normalized.png
│   │   │   │   ├── confusion_matrix.png
│   │   │   │   ├── example.jpg
│   │   │   │   ├── F1_curve.png
│   │   │   │   ├── P_curve.png
│   │   │   │   ├── PR_curve.png
│   │   │   │   ├── R_curve.png
│   │   │   │   ├── results.png
│   │   │   │   └── validation.png
│   │   │   └── sahi_yolov8n/
│   │   │       ├── confusion_matrix_normalized.png
│   │   │       ├── confusion_matrix.png
│   │   │       ├── example.jpg
│   │   │       ├── F1_curve.png
│   │   │       ├── P_curve.png
│   │   │       ├── PR_curve.png
│   │   │       ├── R_curve.png
│   │   │       ├── results.png
│   │   │       └── validation.png
│   │   ├── microscope.jpg
│   │   └── user_interface.png
│   ├── detection/
│   │   ├── base.py
│   │   ├── esp32.py
│   │   ├── iphone.py
│   │   └── webcam.py
│   └── streaming/
│       ├── boards/
│       │   ├── esp32cam_ai_thinker.json
│       │   ├── esp32cam_espressif_esp_eye.json
│       │   ├── esp32cam_espressif_esp32s2_cam_board.json
│       │   ├── esp32cam_espressif_esp32s2_cam_header.json
│       │   ├── esp32cam_espressif_esp32s3_cam_lcd.json
│       │   ├── esp32cam_espressif_esp32s3_eye.json
│       │   ├── esp32cam_freenove_s3_wroom_n8r8.json
│       │   ├── esp32cam_freenove_wrover_kit.json
│       │   ├── esp32cam_m5stack_camera_psram.json
│       │   ├── esp32cam_m5stack_camera.json
│       │   ├── esp32cam_m5stack_esp32cam.json
│       │   ├── esp32cam_m5stack_unitcam.json
│       │   ├── esp32cam_m5stack_unitcams3.json
│       │   ├── esp32cam_m5stack_wide.json
│       │   ├── esp32cam_seeed_xiao_esp32s3_sense.json
│       │   ├── esp32cam_ttgo_t_camera.json
│       │   └── esp32cam_ttgo_t_journal.json
│       ├── html/
│       │   ├── index.html
│       │   └── index.min.html
│       ├── include/
│       │   ├── format_duration.h
│       │   ├── format_number.h
│       │   ├── lookup_camera_effect.h
│       │   ├── lookup_camera_frame_size.h
│       │   ├── lookup_camera_gainceiling.h
│       │   ├── lookup_camera_wb_mode.h
│       │   └── settings.h
│       ├── lib/
│       │   └── rtsp_server/
│       │       ├── library.json
│       │       ├── rtsp_server.cpp
│       │       └── rtsp_server.h
│       ├── src/
│       │   └── main.cpp
│       ├── generate_html.ps1
│       ├── generate_html.sh
│       ├── minify.py
│       └── platformio.ini
├── videos/
│   └── index.html
├── weights/
│   ├── custom_yolov8x_v2.pt.zip
│   ├── custom_yolov8x.pt.zip
│   └── yolov8n_sahi.pt.zip
├── .gitattributes
├── .gitignore
├── environment.yml
└── README.md
</pre>
</details>

## Requirements
<details>
   <summary><b>ESP32-CAM (or similar)</b></summary>
      <ul>
         <li>AI Thinker</li>
         <li>Espressif ESP-EYE</li>
         <li>Espressif ESP32S2-CAM</li>
         <li>Espressif ESP32S3-CAM-LCD</li>
         <li>Espressif ESP32S3-EYE</li>
         <li>Freenove ESP32-WROVER</li>
         <li>M5Stack</li>
         <li>M5Stack ESP32CAM</li>
         <li>M5Stack PSRAM</li>
         <li>M5Stack Unit Cam</li>
         <li>M5Stack Unit CamS3</li>
         <li>M5Stack PSRAM</li>
         <li>M5Stack PSRAM 2.0</li>
         <li>M5Stack WIDE</li>
         <li>Seeed Studio XIAO ESP32S3 Sense</li>
         <li>TTGO T-Camera</li>
         <li>TTGO T-Journal</li>
      </ul>
</details>

- [x] Nikon microscope with 3D printed lens attachment and illuminator
- [x] Micro-USB cable
- [x] [Algae dataset](https://drive.google.com/drive/folders/1gd85o6dpcjDwWJUUi4x9slhjHHuoY4K0)
- [x] [Visual Studio Code](https://code.visualstudio.com/download)
- [x] [PlatformIO plugin for Visual Studio Code](https://platformio.org/install/ide?install=vscode)
- [x] [Roboflow account](https://roboflow.com)
- [x] [Google Colab account](https://accounts.google.com/ServiceLogin?passive=true&continue=https%3A%2F%2Fcolab.research.google.com)
- [x] [Anaconda](https://docs.continuum.io/free/anaconda/install) **OR** [Miniconda](https://docs.conda.io/projects/miniconda/en/latest)

> [!TIP]
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

## Usage
### Detect and Classify Algae
<details open>
   <summary><b>User Interface</b></summary>
   <img align="center" alt="User Interface" src="src/assets/user_interface.png">
</details>

1. Open [`weights`](weights)
2. Choose the algae detection model you want to use

> [!TIP]
> To use your own `.pt` model, add it to [`weights`](weights).
>
> To use an existing model, decompress the `.zip` file to get the `.pt` model.
> * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Nano with [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference): [`yolov8n_sahi.pt.zip`](weights/yolov8n_sahi.pt.zip)
> * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Extra-Large: [`custom_yolov8x.pt.zip`](weights/custom_yolov8x.pt.zip), [`custom_yolov8x_v2.pt.zip`](weights/custom_yolov8x_v2.pt.zip)

3. Open [`base.py`](src/detection/base.py)
4. Set [`MODEL_PATH`](src/detection/base.py#L22) to path of desired `.pt` model
5. Read the following depending on which camera you'll use
   * [ESP32](#esp32)
   * [iPhone](#iphone)
   * [Webcam](#webcam)

#### ESP32
> [!IMPORTANT]
> Current implementation of ESP32-CAM requires WiFi!
>
> Unfortunately, WiFi connections from hotspots or SSOs are not compatible.

1. Click the PlatformIO icon in the activity bar, then click 'Pick a folder'<br>
   <img alt="Open PlatformIO project" height="350" src="src/assets/esp32/platformio_folder.png">
2. Open [`streaming`](src/streaming)<br>
   <img alt="Open `streaming`" height="350" src="src/assets/esp32/open_streaming.png">
3. Make sure the ESP32 is connected to the computer
4. Build and upload code to ESP32
   - Click 'Build' to compile code
   - Click 'Upload' to flash code to ESP32<br>
   <img alt="Build, Upload, Monitor" height="350" src="src/assets/esp32/build_upload_monitor.png">
5. To connect initially to the device, connect to the WiFi network starting with `ESP32CAM-RTSP`<br>
   <img alt="`ESP32CAM-RTSP` network" height="250" src="src/assets/esp32/choose_ap.png">
6. Click 'Change settings' once the browser automatically opens the home page ([`http://192.168.4.1`](http://192.168.4.1))

<img alt="Window popup" height="350" src="src/assets/esp32/ap_popup.png">

7. You **must** fill in all of the following fields:
   - AP (i.e., Access Point) password
   - WiFi SSID
   - WiFi password (if applicable)

> [!NOTE]
> If you ever lose/forget the AP password, click 'Erase flash' (in PlatformIO's extension UI) to erase and reset the device, then follow steps 4 and onwards again.

<img alt="System config" height="350" src="src/assets/esp32/init_config.png">

8. Update the streaming server settings and configure camera options (you can always change them later)

> [!WARNING]
> Very low number for 'JPG quality' (i.e., very high quality) may cause the ESP32 to crash or return no image!

   <details>
      <summary><b>Camera Settings</b></summary>
      <div align="center"><img alt="Camera Settings" src="src/assets/esp32/config.png"></div>
   </details>

9. Scroll down and click 'Apply' to save settings

> [!IMPORTANT]
> You must reset the device in order for the settings to take effect.

10. Disconnect from the current network and reconnect to your WiFi in order to reset ESP32 and connect to the AP

> [!NOTE]
> If the error screen says it's unable to make a connection, try rebooting the ESP32 first (you can do so manually by pressing the 'Reset' button). It'll wait 30 seconds for a connection (configurable).
>
> Connect to the SSID, go to the ESP32's IP address and, anytime you're prompted for credentials, enter `admin` as the username and the AP password for the password.

<img alt="Disconnect" height="350" src="src/assets/esp32/disconnect.png">

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

<img alt="IP Address" src="src/assets/esp32/esp32_ip.png">

12. You can now stream from the ESP32
   - HTTP Motion JPEG Streamer: `http://<ESP32 IP address>/stream`
   - HTTP Image: `http://<ESP32 IP address>/snapshot`
   - RTSP: `rtsp://<ESP32 IP address>:554/mjpeg/1`

> [!CAUTION]
> Anyone with network access to the device can see the streams and images!

   <details>
      <summary><b>Home Page</b></summary>
      <div align="center"><img alt="Home Page" src="src/assets/esp32/index.png"></div>
   </details>

13. Open [`esp32.py`](src/detection/esp32.py) once finished
14. Set [`URL`](src/detection/esp32.py#L3) to ESP32's IP address (i.e., `http://10.0.0.111` in this example)
15. Run [`esp32.py`](src/detection/esp32.py)
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

#### iPhone
1. Open [`iphone.py`](src/detection/iphone.py)
2. Run [`iphone.py`](src/detection/iphone.py)
   * POSIX
      ```sh
      $(which python) src/detection/iphone.py
      ```
   * Windows
      ```sh
      $(where python) src\detection\iphone.py
      ```
3. If successfully connected, your iPhone's screen should look like this:<br>
   <img alt="iPhone connected" height="350" src="src/assets/iphone/iphone_ui_connect.png">
4. Press `q` on your computer or 'Disconnect' on your iPhone to exit the program<br>
   <img alt="iPhone disconnected" height="350" src="src/assets/iphone/iphone_ui_disconnect.png">

#### Webcam
1. Open [`webcam.py`](src/detection/webcam.py)
2. Run [`webcam.py`](src/detection/webcam.py)
   * POSIX
      ```sh
      $(which python) src/detection/webcam.py
      ```
   * Windows
      ```sh
      $(where python) src\detection\webcam.py
      ```

### Training, Validating, and Testing Model
1. Visit [this Google Colab notebook](https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ)
2. Follow the notebook's instructions
3. Run notebook

## Future Work
- [ ] Increase dataset and improve model accuracy and versatility by taking quality images of various types of algae
   - At least [1000 images per class](https://blog.roboflow.com/model-best-practices/#dataset-size) 
   - [All classes are balanced](https://blog.roboflow.com/handling-unbalanced-classes) (i.e., have roughly the same amount of images)
   - [Dr. Schonna R. Manning](https://case.fiu.edu/about/directory/profiles/manning-schonna-r..html) may help with categorizing any algae in new images
- [ ] Connect to ESP32 without a web server (e.g., via USB, etc.), just like Webcam and iPhone OR use RTSP instead of HTTP
- [ ] Heatsink for ESP32 to prevent overheating
- [ ] Use DC-GAN to generate additional synthetic images for training
- [ ] Try different models, such as [RetinaNet](https://paperswithcode.com/method/retinanet) and [YOLOv9](https://docs.ultralytics.com/models/yolov9)
- [ ] Run model on ESP32 rather than on computer
- [ ] Update microscope's 3D printed lens attachment by making it adjustable **AND/OR** create multiple ones for different devices, e.g., iPhone, Android, etc.
- [ ] Add Android compatability (if applicable and/or necessary)

## Further Reading
- [USGS Finds 28 Types of Cyanobacteria in Florida Algal Bloom](https://www.usgs.gov/news/national-news-release/usgs-finds-28-types-cyanobacteria-florida-algal-bloom)
- [Cyanobacteria (Blue-Green Algae)](https://myfwc.com/research/wildlife/health/cyanobacteria/#:~:text=Approximately%2020%20cyanobacteria%20species%20in,than%20one%20type%20of%20toxin)
- [Cyanobacteria of the 2016 Lake Okeechobee and Okeechobee Waterway Harmful Algal Bloom](https://pubs.usgs.gov/publication/ofr20171054)
- [Computer Vision Based Deep Learning Approach for the Detection and Classification of Algae Species Using Microscopic Images](https://www.mdpi.com/2073-4441/14/14/2219)
- Research "[toxic cyanobacteria](https://www.google.com/search?q=toxic+cyanobacteria)"

## Credits
Special thanks to:
- [Dr. Antao Chen](https://ieeexplore.ieee.org/author/37291140300) (product owner) for his mentorship
- [rdgbrian](https://github.com/rdgbrian) (team lead during Fall 2023) for his assistance
- [rzeldent](https://github.com/rzeldent) for [ESP32CAM-RTSP](https://github.com/rzeldent/esp32cam-rtsp/tree/develop), which has been slightly modified and added as a git subtree in [`streaming`](src/streaming)
