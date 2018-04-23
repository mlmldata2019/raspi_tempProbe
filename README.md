# Interfacing computers and electronics

Classroom activities for introduction to using electronics with a Raspberry Pi.

* [Connecting to the Pi](#connecting-to-the-pi)
* [Cloning the GitHub repository](#cloning-the-github-repository)
* [Blinking LED](#Blinking-LED)
* [Reading signals from analog sensors](#reading-signals-from-analog-sensors)
* [Temperature probe](#temperature-probe)

## Connecting to the Pi

In this lab, we will connect to the Raspberry Pi desktop using VNC Viewer, which can be downloaded here:

https://www.realvnc.com/download/viewer/

Each group will need at least one computer that can connect to the Pi over a *wired* Ethernet connection. Once this connection has been made, others can connect to the Pi over a *wireless* connection.

#### Wired connection (required initially)

1. Plug in the Pi to turn it on. It will need a minute or two to boot up.

2. Connect the Ethernet cable between the Pi and a computer.

3. Open VNC viewer and type the IP address in the top address bar. The IP address should be written on the Pi (numbers of the form xxx.xxx.xxx.xxx). When prompted, type the password that is written on the Pi.

#### Wireless connection (optional)

4. If there there is a private wireless network, open the web browser and sign into the network.

5. Find the IP address of the Raspberry Pi:

* On the Raspberry Pi, in the terminal type:
`
ifconfig
`

* In the wlan0 section of the output, the IP address for the wireless connection follows `inet addr`

6. Connect via SSH or VNC, making sure your computer is on the same wireless network.

## Cloning the GitHub repository

Open the terminal on the Raspberry Pi and enter:

`
git clone https://github.com/mlmldata2018/raspi_tempProbe.git
`

Change into the new directory.

## Blinking LED

Python file: [led_control.py](led_control.py)

This Python file contains starter code for controlling the brightness of an LED connected to pin 11 (GPIO17). There is basic code given, and instructions for writing new code.

To edit this file, type in the terminal:

`
idle led_control.py
`

To run this file, type in the terminal:

`
python led_control.py
`

## Reading signals from analog sensors

Python file: [adc_simpletest.py](adc_simpletest.py)

This file prints 10-bit values converted from analog sensor voltages. The analog sensors are connected to an 8-channel MCP3008 analog to digital converter.

To run this file, type in the terminal:

`
python adc_simpletest.py
`

For more information:
https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008

## Temperature probe

Python files:
* [tempProbe.py](tempProbe.py) - 1-Wire temperature probe class
* [mug_temp.py](mug_temp.py) - starter code for recording temperature of a coffee mug

##### 1-Wire temperature probe class for Raspberry Pi

The Python class provides a set a functions to get temperature readings from a 1-wire temperature probe. We will use these commands to write a script that records a time series of data in a text file.

###### Example call

```python
import tempProbe as tp

p = tp.TempProbe()
p.get_temp()
```
