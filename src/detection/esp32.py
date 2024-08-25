"""
Object detection with a livestreaming ESP32-CAM camera.

Simple usage example:
    ```python
    esp32 = ESP32("http://0.0.0.0/stream", "ESP32-CAM Livestream", width = 320, height = 240)
    esp32.run()
    ```

    ```sh
    python esp32.py
    ```
"""
from camera import Camera

URL: str = "http://10.0.0.111/stream"
"""Stream URL"""

class ESP32(Camera):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__ == "__main__":
    # Start detection program
    ESP32(URL, "ESP32-CAM Livestream", width = 320, height = 240).run()