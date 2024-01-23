# **Steps to download and run** 
Before follow these steps please Configure the ESP-IDF [release 5.0](https://github.com/espressif/esp-idf/tree/release/v4.4) environment. <sup>[setting-up ESP-IDF environment](https://www.youtube.com/watch?v=byVPAfodTyY) / [toolchain for ESP-IDF](https://blog.espressif.com/esp-idf-development-tools-guide-part-i-89af441585b) 

### 1. Clone the repo
```bash
git clone https://github.com/rdgbrian/cap-2-project-algea-detection
```

### 2. Update the submodules
```bash
git submodule update --init --recursive 
```

### 3. Change the working directory to model_deployment
```bash 
cd cap-2-project-algea-detection/model_deployment
```

## Only do steps 4-6 if you have UNIX-based OS, else skip to step 7

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

In case found error during the building process [follow the official IDF  guide for more details](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html#build-your-first-project). 
