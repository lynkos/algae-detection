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
5. Update the submodules
    ```
    git submodule update --init --recursive 
    ```
6. Change the working directory to `model_deployment`
     * POSIX
       ```sh
       cd algae-detection/model_deployment
       ```
     * Windows
       ```sh
       cd algae-detection\model_deployment
       ```
7. Create a conda virtual environment from `environment.yml`
   ```
   conda env create -f environment.yml
   ```
8. Activate the virtual environment (`algae_env`)
   ```
   conda activate algae_env
   ```
9. Confirm that the virtual environment (`algae_env`) is active
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
10. Read the files within `documentation` directory for more details

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
