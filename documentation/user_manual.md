# User Manual
## Detect and Classify Algae
1. Open [`weights`](weights)
2. Choose the algae detection model you want to use
   * To use your own `.pt` model, add it to [`weights`](weights)
   * To use an existing model, decompress the `.zip` file to get the `.pt` model
      * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Nano with [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference): [`yolov8n_sahi.pt.zip`](weights/yolov8n_sahi.pt.zip)
      * [YOLOv8](https://docs.ultralytics.com/models/yolov8) Extra-Large: [`custom_yolov8x.pt.zip`](weights/custom_yolov8x.pt.zip)
3. Open [`base.py`](src/detection/base.py)
4. Set [`MODEL_PATH`](src/detection/base.py#L21) to path of desired `.pt` model
5. Read the following depending on which camera you'll use
   * [ESP32](#esp32)
   * [Webcam and/or iPhone](#webcam-andor-iphone)

### ESP32
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

### Webcam and/or iPhone
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

## Training, Validating, and Testing Model
All algae detection models trained and tested for this project have been fine-tuned with:

- [Small dataset of images (~1000 total) manually taken with the modified microscope and ESP32-CAM AI Thinker](https://drive.google.com/drive/folders/1gd85o6dpcjDwWJUUi4x9slhjHHuoY4K0)
- Pre-trained models (i.e., [YOLOv8](https://docs.ultralytics.com/models/yolov8), [RT-DETR](https://docs.ultralytics.com/models/rtdetr), and [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference))

Only the top 2 highest performing algae detection models (i.e., [YOLOv8](https://docs.ultralytics.com/models/yolov8) Nano with [SAHI](https://docs.ultralytics.com/guides/sahi-tiled-inference) and [YOLOv8](https://docs.ultralytics.com/models/yolov8) Extra-Large) have been kept.

### [Google Colab](https://colab.research.google.com) (Recommended)
1. Visit [this Google Colab notebook](https://colab.research.google.com/drive/19X4aGWTeXQbgEKVteR9qrgit67jNxkmJ)
2. Follow the instructions in the notebook
3. Run notebook

### [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
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
6. Read the instructions within the notebook and ensure all necessary constants are set
7. Run [`model-pipeline.ipynb`](src/model_pipeline.ipynb): Click `Run All`
8. Deactivate `algae_env` once finished
   ```
   conda deactivate
   ```

## Additional Resources
- [Running yolo locally on computer (with modifications input from the chip could be possible)](https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993)
- [Creating dataset](https://docs.cogniflow.ai/en/article/how-to-create-a-dataset-for-object-detection-using-the-yolo-labeling-format-1tahk19)
- [Labeling images and creating dataset](https://docs.cogniflow.ai/en/article/how-to-label-images-and-create-your-dataset-for-an-object-detection-ai-model-dcfg1y)
- [Tool for labling](https://labelstud.io)
- [How to do the training](https://docs.ultralytics.com/modes) [fine tuning](https://lablab.ai/t/yolov7)