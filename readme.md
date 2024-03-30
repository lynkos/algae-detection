<!-- # **Steps to download and run** 
Before follow these steps please Configure the ESP-IDF [release 5.0](https://github.com/espressif/esp-idf/tree/release/v4.4) environment. <sup>[setting-up ESP-IDF environment](https://www.youtube.com/watch?v=byVPAfodTyY) / [toolchain for ESP-IDF](https://blog.espressif.com/esp-idf-development-tools-guide-part-i-89af441585b)  -->

<div align="center">
<h1>Algae Detection</h1>
<img alt="Python" src="https://img.shields.io/static/v1?label=Language&style=flat&message=Python+3.11.5&logo=python&color=c7a228&labelColor=393939&logoColor=4f97d1">
<img alt="TensorFlow" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=TensorFlow&logo=tensorflow&color=FF6F00&labelColor=393939&logoColor=FF6F00">
<img alt="OpenCV" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=OpenCV&logo=opencv&color=5C3EE8&labelColor=393939&logoColor=5C3EE8">
<img alt="Keras" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Keras&logo=keras&color=D00000&labelColor=393939&logoColor=D00000">
<img alt="NumPy" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=NumPy&logo=numpy&color=013243&labelColor=393939&logoColor=013243">
<img alt="Jupyter" src="https://img.shields.io/static/v1?label=Packages&style=flat&message=Jupyter&logo=jupyter&color=F37626&labelColor=393939&logoColor=F37626">
<img alt="Shell" src="https://img.shields.io/static/v1?label=Shell&style=flat&message=Bash&logo=gnu+bash&color=4EAA25&labelColor=393939&logoColor=4EAA25">
</div>

<div align="center">
<img alt="Repo Size" src="https://img.shields.io/github/repo-size/lynkos/algae-detection?style=flat&label=Repo+Size&labelColor=393939&color=ff62b1">
<img alt="Commit Activity" src="https://img.shields.io/github/commit-activity/y/lynkos/algae-detection?style=flat&label=Commit+Activity&labelColor=393939&color=b30086">
<img alt="Last Commit" src="https://img.shields.io/github/last-commit/lynkos/algae-detection?style=flat&label=Last+Commit&labelColor=393939&color=be0000">
</div>

## Overview
Automatically detect and classify different species of algae from water samples at a reasonable speed in real-time using a convolutional neural net.

## Installation

### 1. Clone the repo
```bash
git clone https://github.com/lynkos/algae-detection.git
```

### 2. Update the submodules
```bash
git submodule update --init --recursive 
```

### 3. Change the working directory to model_deployment
```bash 
cd algae-detection/model_deployment
```

### 4. Install the required packages
```bash
conda env create -f environment.yml
```

### 5. Activate the virtual environment
```bash
conda activate algae_env
```

### 6. Confirm that the virtual environment is active
- If active, the virtual environment's name should be in parentheses () or brackets [] before your command prompt, e.g.
    ```bash
    (algae_env) $
    ```
- If necessary, see which environments are available and/or currently active (active environment denoted with asterisk (*))
    ```bash
    conda info --envs
    ```
    **OR**
    ```bash
    conda env list
    ```

### 7. Read the documentation
Read the files within `documentation` directory for more details

<!-- ## Only do steps 4-6 if you have UNIX-based OS, else skip to step 7

### 4. (Optional) Add `export.sh` command to shell profile
```bash
alias get_idf='. $HOME/esp/esp-idf/export.sh'
```

### 5. (Optional) Restart terminal OR run `source` command
```bash
source <PATH_TO_PROFILE>
```

### 6. (Optional) Run `export.sh` command
```bash
get_idf
```

### 7. Reconfigure the Cmake 
```bash 
idf.py reconfigure 
```

### 8. Select the target ESP32 (Make sure the device is connected!)
```bash 
idf.py set-target esp32
```

### 9. Run project configuration
```bash
idf.py menuconfig
```

### 10. Select the following options, then save and quit
```
Serial flasher config > Flash size > 4 MB
```

### 11. Build the project
```bash
idf.py build
```

### 12. Flash and monitor the project (`PATH_TO_ESP_DEVICE` = `COM4` for Windows)
```bash
idf.py -p PATH_TO_ESP_DEVICE flash
idf.py -p PATH_TO_ESP_DEVICE monitor
```

In case found error during the building process [follow the official IDF  guide for more details](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html#build-your-first-project).  -->
