# ESP32CAM-RTSP

Simple [RTSP](https://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol), [HTTP Motion JPEG Streamer](https://en.wikipedia.org/wiki/Motion_JPEG), and image server for ESP32-CAMs that's configurable via a web interface.

- RTSP
  - Industry standard protocol that allows many CCTV systems and applications (e.g., [VLC](https://www.videolan.org/vlc), etc.) to connect directly to the ESP32-CAM camera stream
  - Stream directly to a server using [ffmpeg](https://ffmpeg.org)
  - Makes ESP32-CAM a camera server allowing recording and the stream can be stored on a disk and replayed later
  - URL: `rtsp://<ip address>:554/mjpeg/1`

- HTTP Motion JPEG Streamer
  - Watch camera stream in real-time directly in your browser
  - URL: `http://<ip address>/stream`

- HTTP Image
  - Returns a JPEG image from the camera via HTTP
  - URL: `http://<ip address>/snapshot`

The software provides a **configuration web server** that can be used to (1) get information about the device's state, WiFi connection, and camera, (2) set the streaming server's settings, and (3) configure a wide variety of camera options. It also provides an mDNS server to be easily discoverable on the local network. It advertises HTTP (port 80) and RTSP (port 554).

## Compile and Deploy

1. Enter [`streaming`](src/streaming) directory

```sh
cd streaming
```

2. Open the project in a new window
3. Run the following tasks using the `Terminal -> Run Task` or `CTRL + ALT + T` command in the menu (or use the icons below on the toolbar) and make sure the ESP32-CAM is in download mode during the uploads

- PlatformIO: Build
- PlatformIO: Upload
- PlatformIO: Monitor (OPTIONAL)

## Setup

After the programming of the ESP32, there is no configuration present. This needs to be added.
To connect initially to the device open the WiFi connections and select the WiFi network / access point called **ESP32CAM-RTSP**.
Initially there is no password present.

After connecting, the browser should automatically open the status page.
In case this does not happens automatically, connect to [`http://192.168.4.1`](http://192.168.4.1).
This page will display the current settings and status. On the bottom, there is a link to the config. Click on this link.
This link brings up the configuration screen when connecting fot the first time.

![Configuration screen](/src/assets/esp32/config.png)

Configure at least:

- The access point to connect to. No dropdown is present to show available networks!
- A password for accessing the Access point (AP) when starting. (required)
- Type of the ESP32-CAM board

When finished press `Apply` to save the configuration. The screen will redirect to the status screen.
Here it is possible to reboot the device so the settings take effect.
It is also possible to restart manually by pressing the reset button.

## Connect to the Configuration

After the initial configuration and the device is connected to an access point, the device can be configured over http.

When a connection is made, the status screen is shown.

![Status screen](/src/assets/esp32/index.png)

In case changes have been made to the configuration, this is shown and the possibility to restart is given.

Clicking on the `change configuration` button will open the configuration. It is possible that a password dialog is shown before entering.
If this happens, for the user enter 'admin' and for the password the value that has been configured as the Access Point password.

## Connect to Stream

The streaming server is available using a normal web browser at:

[http://10.0.0.114/stream](http://10.0.0.114/stream)

> [!WARNING]
> There is no password present!
> Anyone with network access to the device can see the streams and/or images!

## API

There is a minimum API present to perform some tasks using HTTP requests. For some requests authentication is required.
The authentication used is basic authentication. The user is always admin and the password the access point key.
If using a browser, remember that the authentication is stored in the browser session so needs to be entered only once.

### `GET: /restart`

Calling this URL will restart the device. Authentication is required.

### `GET: /config`

Calling this URL will start the form for configuring the device in the browser. Authentication is required.

### `GET: /snapshot`

Calling this URL will return a JPEG snapshot of the camera in the browser.
This request can also be used (for example using cURL) to save the snapshot to a file.

## Notes / Issues

- For the JPEG quality setting, a lower number means higher quality.
  Be aware that a very high quality (low number) can cause the ESP32 cam to crash or return no image
- The red LED on the back of the device indicates the device is not connected
- Sometimes after configuration a reboot is required
  If the error screen is shown that it is unable to make a connection, first try to reboot the device,
- When booting, the device waits 30 seconds for a connection (configurable).
  You can make a connection to the SSID and log in using the credentials mentioned in the next bullet
- When connected, go to the device's IP and, when prompted for the credentials, enter 'admin' and the AP password
  This is a **required** field before saving the credentials
- When the password is lost, a fix is to completely erase the ESP32 using the ```pio run -t erase``` command.
  This will reset the device including configuration.
  However, after erasing, re-flashing of the firmware is required.
- When finished configuring for the first time and the access point is entered, disconnect from the wireless network provided by the device.
  This should reset the device and connect to the access point.
  Resetting is also a good alternative...

## Credits

[ESP32CAM-RTSP](https://github.com/rzeldent/esp32cam-rtsp/tree/develop) depends on PlatformIO, Bootstrap 5, and [Micro-RTSP](https://github.com/geeksville/Micro-RTSP) by [Kevin Hester](https://github.com/geeksville).