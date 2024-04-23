# Installation Guide
## Requirements
- <details>
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

> [!IMPORTANT]
> Due to the [large] size of the repo, you may get errors such as:
> 
> <pre>error: RPC failed; curl 56 Recv failure: Connection reset by peer error: 6022 bytes of body are still expected fetch-pack: unexpected disconnect while reading sideband packet fatal: early EOF fatal: fetch-pack: invalid index-pack output</pre>
>
> If this is the case, please download [Git LFS](https://git-lfs.com) and try cloning again. If you're still getting errors, consider [cloning via SSH](https://github.com/git-guides/git-clone#git-clone-with-ssh) (`git clone git@github.com:lynkos/algae-detection.git`) or [manually downloading the repo as a `.zip` file](https://github.com/lynkos/algae-detection/archive/refs/heads/main.zip) and decompressing it.

5. Create conda virtual environment from [`environment.yml`](/environment.yml)
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
