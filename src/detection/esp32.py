from base import Camera

URL = "http://10.0.0.114/stream"
"""Stream URL"""

if __name__ == "__main__":
    # Start algae detection program
    Camera(URL, "ESP32 Stream", width = 320, height = 240).run()