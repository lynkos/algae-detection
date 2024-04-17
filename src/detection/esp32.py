from base import Camera

URL = "http://10.0.0.114/stream"
"""Stream URL"""

Camera(URL, "ESP32 Stream").run()
"""Start algae detection program"""