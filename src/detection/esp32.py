from base import Camera

URL = "http://10.0.0.134/stream"
"""Stream URL"""

Camera(URL, "ESP32 Stream").run()
"""Start algae detection program"""