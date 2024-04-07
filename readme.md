<!-- # **Steps to download and run** 
Before follow these steps please Configure the ESP-IDF [release 5.0](https://github.com/espressif/esp-idf/tree/release/v4.4) environment. <sup>[setting-up ESP-IDF environment](https://www.youtube.com/watch?v=byVPAfodTyY) / [toolchain for ESP-IDF](https://blog.espressif.com/esp-idf-development-tools-guide-part-i-89af441585b)  -->

<div align="center">
<h1>Algae Detection</h1>
<img alt="Python" src="https://img.shields.io/static/v1?label=Language&style=flat&message=Python+3.11.5&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1">
<img alt="Shell" src="https://img.shields.io/static/v1?label=Shell&style=flat&message=Bash&logo=gnu+bash&color=b30086&labelColor=393939&logoColor=b30086">
<img alt="Conda" src="https://img.shields.io/static/v1?label=Package+Manager&style=flat&message=Conda&logo=anaconda&color=44A833&labelColor=393939&logoColor=44A833">
<br>
<img alt="Keras" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Keras&logo=keras&color=D00000&labelColor=393939&logoColor=D00000">
<img alt="PyTorch" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=PyTorch&logo=pytorch&color=EE4C2C&labelColor=393939&logoColor=EE4C2C">
<img alt="TensorFlow" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=TensorFlow&logo=tensorflow&color=FF6F00&labelColor=393939&logoColor=FF6F00">
<img alt="Jupyter" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Jupyter&logo=jupyter&color=F37626&labelColor=393939&logoColor=F37626">
<img alt="Matplotlib" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Matplotlib&color=11557c&labelColor=393939&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxODAiIGhlaWdodD0iMTgwIiBzdHJva2U9ImdyYXkiPgo8ZyBzdHJva2Utd2lkdGg9IjIiIGZpbGw9IiNGRkYiPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSI4OCIvPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSI2NiIvPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSI0NCIvPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSIyMiIvPgo8cGF0aCBkPSJtOTAsMnYxNzZtNjItMjYtMTI0LTEyNG0xMjQsMC0xMjQsMTI0bTE1MC02MkgyIi8+CjwvZz48ZyBvcGFjaXR5PSIuOCI+CjxwYXRoIGZpbGw9IiM0NEMiIGQ9Im05MCw5MGgxOGExOCwxOCAwIDAsMCAwLTV6Ii8+CjxwYXRoIGZpbGw9IiNCQzMiIGQ9Im05MCw5MCAzNC00M2E1NSw1NSAwIDAsMC0xNS04eiIvPgo8cGF0aCBmaWxsPSIjRDkzIiBkPSJtOTAsOTAtMTYtNzJhNzQsNzQgMCAwLDAtMzEsMTV6Ii8+CjxwYXRoIGZpbGw9IiNEQjMiIGQ9Im05MCw5MC01OC0yOGE2NSw2NSAwIDAsMC01LDM5eiIvPgo8cGF0aCBmaWxsPSIjM0JCIiBkPSJtOTAsOTAtMzMsMTZhMzcsMzcgMCAwLDAgMiw1eiIvPgo8cGF0aCBmaWxsPSIjM0M5IiBkPSJtOTAsOTAtMTAsNDVhNDYsNDYgMCAwLDAgMTgsMHoiLz4KPHBhdGggZmlsbD0iI0Q3MyIgZD0ibTkwLDkwIDQ2LDU4YTc0LDc0IDAgMCwwIDEyLTEyeiIvPgo8L2c+PC9zdmc+">
<img alt="NumPy" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=NumPy&logo=numpy&color=013243&labelColor=393939&logoColor=013243">
<img alt="Ultralytics YOLOv8" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Ultralytics+YOLOv8&color=042AFF&labelColor=393939&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAyIiBoZWlnaHQ9IjUxMiIgdmlld0JveD0iMCAwIDUwMiA1MTIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8xMF8xNjgpIj4KPHBhdGggZD0iTTExNy41MTkgMC4wMDE2NDAzMkM1Mi43MTgyIDAuMDAxNjQwMzIgMi4zNzcwMmUtMDUgNTIuNzQ0MiAyLjM3NzAyZS0wNSAxMTcuNTc0QzIuMzc3MDJlLTA1IDE4Mi4zOTkgNTIuNzE4MiAyMzUuMTQzIDExNy41MTkgMjM1LjE0M0MxODIuMzIxIDIzNS4xNDMgMjM1LjAzOSAxODIuMzk5IDIzNS4wMzkgMTE3LjU3NEMyMzUuMDM5IDUyLjc0NDIgMTgyLjMyMSAwLjAwMTY0MDMyIDExNy41MTkgMC4wMDE2NDAzMloiIGZpbGw9IiMwQjIzQTkiLz4KPHBhdGggZD0iTTI1MC40OCAzNjguMTYxQzIwOC4xNDggMzY4LjE2MSAxNjguMTQ5IDM1Ny40MzggMTMzLjAzNyAzMzguNjExVjM5MS45NTJDMTMzLjAzNyA0NTYuNjgxIDE4NC43IDUxMC4zODkgMjQ5LjM5OCA1MTEuMDE1QzMxNC43MyA1MTEuNjQ2IDM2OC4wNzkgNDU4LjY2MiAzNjguMDc5IDM5My40NTFWMzM4LjU2MUMzMzIuOTM0IDM1Ny40MzUgMjkyLjg3IDM2OC4xNjEgMjUwLjQ4IDM2OC4xNjFaIiBmaWxsPSIjMEIyM0E5Ii8+CjxwYXRoIGQ9Ik0yNjUuODU4IDExNy41ODdDMjY1LjczNiAxOTkuMzc1IDE5OS4zNjkgMjY1Ljc5NyAxMTcuMzI0IDI2NS45OTdDODUuNjc0NyAyNjYuMDc5IDU1Ljk3NTYgMjU2LjIyMiAzMS43NCAyMzkuMDE0Qzc0LjY5NTMgMzE1LjgzMyAxNTYuNjYxIDM2OC4yMTEgMjUwLjM4NCAzNjguMDI5QzM4Ni41MzIgMzY4LjEzNyA0OTguODc1IDI1Ny4yNDIgNTAxLjE0NCAxMjEuMjMyTDUwMC44MjIgMTIwLjk0MUM1MDAuOTU2IDExNy41NTIgNTAwLjc5IDEyMC4zMjggNTAwLjk1NiAxMTcuNTUyQzUwMS4wMjEgNTIuNjc2NyA0NDguMjIyIC0wLjI3MTUwMiAzODMuNjk3IC0wLjA0NTYzMDNDMzE4LjU1OCAwLjIxMTU5NyAyNjUuOTIzIDUyLjcxMSAyNjUuODU4IDExNy41ODdaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMTBfMTY4KSIvPgo8L2c+CjxkZWZzPgo8bGluZWFyR3JhZGllbnQgaWQ9InBhaW50MF9saW5lYXJfMTBfMTY4IiB4MT0iMTQyLjEzNyIgeTE9IjM2My44NyIgeDI9IjQzMy4xMjMiIHkyPSI0MS42NjY1IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CjxzdG9wIHN0b3AtY29sb3I9IiMwOURCRjAiLz4KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjMEIyM0E5Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTBfMTY4Ij4KPHJlY3Qgd2lkdGg9IjUwMiIgaGVpZ2h0PSI1MTIiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==">
<img alt="Roboflow" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Roboflow&color=6706CE&labelColor=393939&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI1LjMuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCA2MDAgNjAwIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA2MDAgNjAwOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+Cgkuc3Qwe2ZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO2ZpbGw6IzY3MDZDRTt9Cgkuc3Qxe2ZpbGwtcnVsZTpldmVub2RkO2NsaXAtcnVsZTpldmVub2RkO2ZpbGw6I0ZGRkZGRjt9Cjwvc3R5bGU+CjxnPgoJPGNpcmNsZSBjbGFzcz0ic3QwIiBjeD0iMzAwIiBjeT0iMzAwIiByPSIzMDAiLz4KPC9nPgo8Zz4KCTxwYXRoIGNsYXNzPSJzdDEiIGQ9Ik0yNzkuMzQsMjY3LjY3YzI3LjctMjEuNTgsMTUuNTUtNTEuMTEtMzAuMjQtNDUuNGMtNTMuMDMsNi42LTEyMC42Miw1OC40NS0xMzcuNDYsMTIwLjcKCQljLTEuMzgsNS4wOS0yLjQ1LDEwLjI3LTMuMTksMTUuNWMtMC43Myw1LjE1LTEuMTIsMTAuMzUtMS4xNywxNS41NWMtMC4wNSw1LjE1LDAuMjUsMTAuMywwLjg5LDE1LjQKCQljMC42NCw1LjExLDEuNjQsMTAuMTcsMi45OCwxNS4xNGMxLjM2LDUuMDMsMy4wNiw5Ljk3LDUuMDksMTQuNzZjMi4wOSw0LjkyLDQuNTEsOS42OCw3LjI0LDE0LjI2YzIuODMsNC43Niw1Ljk4LDkuMzEsOS40LDEzLjY0CgkJYzExLjY3LDE0Ljc4LDI2LjY1LDI3LjE2LDQyLjYzLDM3LjAyYzMuNDYsMi4xNCw3LjE4LDQuMjEsMTEuMjUsNC40MWM1Ljk0LDAuMjgsMTAuNDQtNC40NCwxMC42OC0xMC4yMwoJCWMwLjA5LTIuMTgtMC40Ni00LjI0LTEuNDYtNmMtMTMuNDItMjMuNjctMjQuNTItNTguODEtMjIuMjQtODAuOTlDMTc5LjQzLDMzNi4yOSwyMzUuMjgsMzAxLjk4LDI3OS4zNCwyNjcuNjd6Ii8+Cgk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNNTAwLjI4LDM2My44NGMtMi45LTYuOTEtMTAuMTYtMTAuODEtMTcuNTEtMTAuMTVjLTUuMDIsMC40NS05LjE3LDMuMTMtMTIuNTUsNi42OAoJCWMtNS40OSw0Ljk3LTkuMzEsMTEuODktMTMuNDMsMTcuOTFjLTQuODYsNy4wOC05Ljk0LDE0LjAyLTE1LjQxLDIwLjYzYy0xMC44LDEzLjA0LTIzLjI0LDI0Ljc5LTM3Ljc2LDMzLjYxCgkJYy0yNC42MywxNC45NS00Ny4xNywyMi4xMi03NC4yNyw4LjMxYy0xOS44My0xNS44Ni0xMy4xMy0zNC42LDMuMjktNDkuODdjMjguMDgtMjYuMSw2MS45My00NC40Miw4OC41Mi03Mi40NAoJCWMyNS0yNi4zNCw0Ny4wNS01OS4xMSw1Mi4yNC05NS43OGMxLjQ2LTEwLjI3LDEuNDgtMjAuNzQtMC4xNy0zMWMtNy44LTQ4LjMxLTUxLjQ4LTc4Ljk3LTk1LjU5LTkyLjAxCgkJQzMyMS40Nyw4My4xMywyNTkuNiw4OCwyMDYuNDgsMTEyLjU2Yy0yMS44NiwxMC4xMS00Mi4yMywyMy42NS01OS45NCwzOS45OGMtNy44NSw3LjI0LTE1LjI0LDE1LjAxLTIyLjEsMjMuMgoJCWMtMTEuMSwxMy4yNy0yMy43MywyOC43Ny0yNS44OSw0Ni41N2MtMS4zMywxMC45OSw4LjU4LDE4LjU5LDE4Ljk5LDE3LjE4YzYuOTgtMC45NCwxMy4xNi01LjE1LDE4LjMtOS43NAoJCWM1Ljk3LTUuMzMsMTEuNDUtMTEuMjUsMTcuMjEtMTYuODJjMTcuMzgtMTYuODIsMzUuOTQtMzIuNDcsNTguMDEtNDIuNzljMjguMTEtMTMuMTUsNTkuNjEtMTkuNTUsOTAuNi0xNi4zMgoJCWMzMS40MywzLjI3LDY5LjY3LDE3LjQ0LDgxLjE1LDQ5Ljk4YzExLjk3LDMzLjk3LTEzLjczLDY3LjM2LTM3LjE4LDg5LjA2Yy0zOC4yOSwzNS40NC0xMTAuOTksNzEuNjMtMTAyLjk4LDEzNC4xOQoJCWM0LjI5LDMzLjUxLDI4LjQsNjIuMTksNTkuMjQsNzQuOTZjNTMuNjYsMjIuMjMsMTExLjc0LTQuODQsMTQ4Ljg5LTQ2LjE4YzEyLjQ2LTEzLjI0LDMwLjM4LTM1LjgyLDQ2LjY4LTY5LjQ2CgkJQzUwMC42MSwzNzkuODQsNTAzLjIzLDM3MC44Nyw1MDAuMjgsMzYzLjg0eiIvPgo8L2c+Cjwvc3ZnPg==">
<img alt="OpenCV" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=OpenCV&logo=opencv&color=5C3EE8&labelColor=393939&logoColor=5C3EE8">
</div>

## Overview
Automatically detect and classify different species of algae from water samples at a reasonable speed in real-time using a convolutional neural net.

## Requirements
- [x] [Anaconda](https://docs.continuum.io/free/anaconda/install) **OR** [Miniconda](https://docs.conda.io/projects/miniconda/en/latest)
> [!NOTE]
> If you have trouble deciding between Anaconda and Miniconda, please refer to the table below
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
3. Enter the directory where you want the repository (`algae-detection`) to be cloned
     * POSIX
       ```sh
       cd ~/path/to/directory
       ```
     * Windows
       ```sh
       cd C:\Users\user\path\to\directory
       ```
4. Clone the repository (`algae-detection`)
   ```
   git clone https://github.com/lynkos/algae-detection.git
   ```
5. Change the working directory to `model_deployment`
     * POSIX
       ```sh
       cd algae-detection/model_deployment
       ```
     * Windows
       ```sh
       cd algae-detection\model_deployment
       ```
6. Create a conda virtual environment from `environment.yml`
   ```
   conda env create -f environment.yml
   ```
7. Activate the virtual environment (`algae_env`)
   ```
   conda activate algae_env
   ```
8. Confirm that the virtual environment (`algae_env`) is active
     * If active, the virtual environment's name should be in parentheses () or brackets [] before your command prompt, e.g.
       ```
       (algae_env) $
       ```
     * If necessary, see which environments are available and/or currently active (active environment denoted with asterisk (*))
       ```
       conda info --envs
       ```
       **OR**
       ```
       conda env list
       ```
9. Read the files within `documentation` directory for more details

<!-- ## Only do steps 4-6 if you have UNIX-based OS, else skip to step 7

### 4. (Optional) Add `export.sh` command to shell profile
```sh
alias get_idf='. $HOME/esp/esp-idf/export.sh'
```

### 5. (Optional) Restart terminal OR run `source` command
```sh
source <PATH_TO_PROFILE>
```

### 6. (Optional) Run `export.sh` command
```
get_idf
```

### 7. Reconfigure the Cmake 
```
idf.py reconfigure 
```

### 8. Select the target ESP32 (Make sure the device is connected!)
```
idf.py set-target esp32
```

### 9. Run project configuration
```
idf.py menuconfig
```

### 10. Select the following options, then save and quit
```
Serial flasher config > Flash size > 4 MB
```

### 11. Build the project
```
idf.py build
```

### 12. Flash and monitor the project (`PATH_TO_ESP_DEVICE` = `COM4` for Windows)
```
idf.py -p PATH_TO_ESP_DEVICE flash
idf.py -p PATH_TO_ESP_DEVICE monitor
```

In case found error during the building process [follow the official IDF  guide for more details](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html#build-your-first-project).  -->

## Usage
WIP
<!-- ### [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) (Recommended)
1. Open the Command Palette in [Visual Studio Code](https://code.visualstudio.com/download) with the relevant keyboard shortcut
    * Mac
      ```
      ⌘ + Shift + P
      ```
    * Windows
      ```
      CTRL + Shift + P
      ```
2. Search and select `Python: Select Interpreter`
3. Select the virtual environment (`algae_env`)
4. Open `algae-classification.ipynb` and/or `yolo-computer.py`
5. Confirm `algae_env` is the selected [kernel](https://docs.jupyter.org/en/latest/install/kernels.html)
6. Run program(s)
   * `algae-classification.ipynb`: Click `Run All`
   * `yolo-computer.py`: Click `▷` (i.e. `Play` button) in the upper-right corner
7. Deactivate the virtual environment (`algae_env`) when you're finished
   ```
   conda deactivate
   ```

### Command Line
#### Python
1. Run `yolo-computer.py`
   * POSIX
      ```
      $(which python) yolo-computer.py
      ```
   * Windows
      ```
      $(where python) yolo-computer.py
      ```
2. Deactivate the virtual environment (`algae_env`) when you're finished
   ```
   conda deactivate
   ```

#### Jupyter Notebook
1. Install `ipykernel` in the virtual environment (`algae_env`)
   ```
   conda install -n algae_env ipykernel
   ```
2. Add the virtual environment (`algae_env`) as a Jupyter kernel
   ```
   python -m ipykernel install --user --name=algae_env
   ```
3. Open `algae-classification.ipynb` in the currently running notebook server, starting one if necessary
   ```
   jupyter notebook algae-classification.ipynb
   ```
4. Select the virtual environment (`algae_env`) as the kernel before running `algae-classification.ipynb`
5. Deactivate the virtual environment (`algae_env`) when you're finished
   ```
   conda deactivate
   ``` -->
