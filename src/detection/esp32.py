from base import Camera

URL = "http://10.0.0.114/stream"
"""Stream URL"""

Camera(URL, "ESP32 Stream", width = 320, height = 240).run()
"""Start algae detection program"""