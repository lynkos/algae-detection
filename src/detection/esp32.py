from Camera import Camera

URL: str = "http://10.1.10.114/stream"
"""Stream URL"""

if __name__ == "__main__":
    # Start detection program
    Camera(URL, "ESP32 Stream", width = 320, height = 240).run()