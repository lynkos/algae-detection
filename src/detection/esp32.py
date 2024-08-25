"""
Object detection with a livestreaming ESP32-CAM camera.

Simple usage example:
    ```python
    esp32 = camera.Camera("http://0.0.0.0/stream", "ESP32-CAM Livestream", width = 320, height = 240)
    esp32.run()
    ```
"""
from camera import Camera

URL: str = "http://10.1.10.114/stream"
"""Stream URL"""

if __name__ == "__main__":
    # Start detection program
    Camera(URL, "ESP32-CAM Livestream", width = 320, height = 240).run()
