# Instalation Guide

## Model Development Notebook (webserver)
open the model_deployment directory and move the files there (the notebook and algea_dataset) to a google drive directory. With some minor changes to the notebook which is just updating the path of the the dataset depending on where you put it the code would be working if you run it on google colab. To run simply click on the file twice and google colab should automantically open.

![](./_static/colab.png)
    

## Camera Web App
- First make sure that your ESP-32 chip is mounted onto the microscope and that it is connected to your local computer through a USB cable.

- To run the camera-web server onto the chip you would need to download the Arduino IDE to compile and flash the web server code onto the chip. You can install Arduino IDE from https://www.arduino.cc/en/software

- Go to file, preferences, and add the additional board manager url https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

![](./_static/adrino_ide_preferences.png)

![](./_static/arduino_url.png)
    
- To download the camera web server code you can clone our repository to access it https://github.com/rdgbrian/cap-2-project-algea-detection, and open the webserver code in your IDE. Or alternatively you can access it though the IDE. You can access it though the IDE by setting the current board to be the ESP32 Dev Module. Then selecting file->examples->ESP32->Camera->CameraWebServer

![](./_static/camera_server.png)

Once selected be sure to use the AI Thinker model and not the ESP 32 Eye cam model: 

![](./_static/corrected_web.png)

You will then need to fill out the required credentials which will be the internet connection name under ssid and password under the password

![](./_static/wifi_pwd.png)

- Once you are ready to run your program. Check if the correct bord and port (USB connection) is selected by pressing the button that has the usb symbol in the top middle of your screen.

![](./_static/port_chip.png)
    
- Then compline and flash your code onto the chip.
Open the serial monitor in the IDE to see the input from the chip. This input  will provide a link to access the live camera input. Copy and paste this link onto your browser to interact and view the live video.

## Model Deployment Program (model_deployment)
The model deployment code runs using ESP-IDF instead of the Arduino IDE. To install ESP-IDF download the installer in here: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/#manual-installation. The model deployment program **ONLY** works on ESP-IDF version 5.0.x. This program is known to work on version 5.0.4. If you install the newer versions like 5.1.2 you will encounter issues. In this instalation guide I will.

### ESP-IDF Windows instalation
Grab the installer here https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html.
Go though all the steps and leave everything default **EXCEPT** remeber to install the version 5.0.4

![](./_static/idf_wind.png)

### ESP-IDF Linux instalation
- Ubuntu and Debian
```
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv 
cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```
- CentOS 7 & 8
```
sudo yum -y update && sudo yum install git wget flex bison gperf 
python3 cmake ninja-build ccache dfu-util libusbx
```
- Arch
```
sudo pacman -S --needed gcc git make flex bison gperf 
python cmake ninja ccache dfu-util libusb
```
### Downloading ESP-DL
Finally we need to download ESP-DL in `model_deployment\components`. clone the [ESP-DL](https://github.com/espressif/esp-dl) from the Github repository. 
```bash
cd model_deployment\components
git clone --recursive https://github.com/espressif/esp-dl.git

```

## Model Quantize Program (model_quantize)
The code found in this direcotry is used to quantize the onnx file that was produced in the [Model Development Notebook](#Model-Development-Notebook). To run this you will first need to install anaconda which is a disribution of python that will help you manage the packages that you want to install. Then install the appropriate packages and python version listed.

Create a new environment in anaconda and install the follwing packages and python version.

| Module     | How to install  |
| :-----------: | :-----------: |
| Python == 3.7                   |
| Numba == 0.53.1        |   `pip install Numba==0.53.1`           |
| ONNX == 1.9.0           |   `pip install ONNX==1.9.0`        |
|ONNX Runtime == 1.7.0       |  `pip install ONNXRuntime==1.7.0`         |
|ONNX Optimizer == 0.2.6            |  `pip install ONNXOptimizer==0.2.6`        |


To quickly configure your conda enviornemnt and install the requiered packages run the following comands:
First make sure you are in the `model_quantize` directory.
```
cd model_quantize
```
Then run these comands:
```bash
conda create -n <env-name> python=3.7
pip install -r requirements.txt
conda activate <env-name>
```

## Anaconda Guide
After you have installed anaconda using the instructions bellow then you can create and manage your environments using the following comands. For more information on how to manage and set up your conda enviornment 

To create an environement:
```bash
conda create -n <env-name> python=3.9
```
To use your environment you would type the following command:
```bash
conda activate <env-name>
```

In our project we have a file called `requierments.txt` which has the informations on what packages needs to be installed to use this file you would need to run the following comand and all the packages listed in the file would be automatically installed into your conda environment for you.

```bash
pip install -r requirements.txt
```

To use your enviroment you would need to run:
```bash
conda install -c conda-forge <package-name>
```
or if you prefer you can also install with pip
```bash
pip install <package-name>
```
When in doubt you can always search "pip install \<package-name\>" or "anaconda install \<package-name\>" in your browser and the appropriate way to install your package should pop up.

Once you've activated your enviornemnt you can add packages using either the following comands

Incase this is your first time using anaconda you can follow the instalation guide bellow.

#### Installing on windows

##### Download Anaconda

 - Go to https://www.anaconda.com/download and download anaconda  

![](./_static/anaconda_install.png)

The installer should look like this when you open it up. Go though it and you can leave all the settings on default.
##### Adding Anaconda To Path

```bash
where conda 
where python
```
Notice where `python.exe` and `conda.exe` in installed. For example in my command line the following output was shown.

![](./_static/where_anaconda.png)

`conda.exe` would be in  `C:\Users\<user>\anaconda3`
`python.exe` would be in `C:\Users\<user>\anaconda3\Scripts`

Finally edit your systems enviornment variables by adding the following directories we found above to path.

First you open System Properties. You can do this by searching 

![](./_static/system_properties.png)

![](./_static/environment_variables.png)

![](./_static/edit_path.png)

#### Installing on linux
##### Download Miniconda Installer
```Bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
-O /opt/miniconda-installer.sh
```
##### Install Miniconda
```Bash
bash /opt/miniconda-installer.sh
```

```
Miniconda3 will now be installed into this location:
/root/miniconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below
```
Just press ENTER and continue.

```
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>>
```
Type ‘yes’, then hit ENTER. You should see this as an output.

you should add the path to your .bashrc file by running the command:
```
echo ‘export PATH=”/path/to/miniconda3/bin:$PATH”’ >> ~/.bashrc
```

Its important to note that miniconda doesnt come with pip so you would have do download it using the following comand.
```
sudo apt install python3-pip
```