# raspiSurveillance
Raspberry Pi Video Streaming with Pan-Tilt Control.

## Objectives
- To experiment with the new raspberry pi 3.
- To develop a surveillance mechanism with automatic recordings.
- To be able to interact with the camera, panning and tilting it remotely.

## HW Used
- Raspberry Pi 3 - Model B - ARMv8 with 1G RAM[ID:3055]
- USB WiFi (802.11b/g/n) Module with Antenna for Raspberry Pi[ID:1030] 
- Mini Pan-Tilt Kit - Assembled with Micro Servos[ID:1967]
- Adafruit 16-Channel PWM / Servo HAT for Raspberry Pi - Mini Kit[ID:2327]
- Raspberry Pi Camera Board v2 - 8 Megapixels[ID:3099]
- Aluminum Heat Sink for Raspberry Pi 3 - 14 x 14 x 8mm[ID:3083]
- Pi Model B+ / Pi 2 / Pi 3 Case Base - Clear[ID:2253]
- Flex Cable for Raspberry Pi Camera - 24" / 610mm[ID:1731]

## SW used
- Raspbian Jessie, Kernel version 4.4 from www.raspberrypi.org/downloads/raspbian
- netcat 

## How to
#### Setting up the Pi for development (Optional)
With these steps, the Pi will start up a vnc server once you plg it in and even publish its local IP adrresses to help you connect faster.
- Create the db on a public server importing _publishIP.sql_, this is where the IP(s) will be published.
- Fill in the _secret.py_ file with the db connection parameters (used only by _publishIP.py_).
- Run _publishIP.py_ as well as this https://www.raspberrypi.org/documentation/remote-access/vnc/ at startup (you can use init.d or crontab).

### Setting up the Relay Server
- 

### Setting up the client
- 