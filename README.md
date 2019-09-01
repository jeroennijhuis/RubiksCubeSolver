# RubiksCubeSolver ( TO BE CONTINUED )
Rubiks cube solving robot ( Raspberry Pi)

Here you will find a complete walkthrough and all the requirements needed to set up your own robot!

### Requirements

* Raspberry Pi 3 ( incl. SD card >= 8 Gb)
* 6 x Nema 17 stepper motor
* External power supply (12V 15A)


### Walkthrough

1. Setup your Raspberry Pi 3 Software
* Make sure an internet connection is established.
* install the [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) on your SD card using Win32DiskManager for example (tested version: April 2017)
* Configure your raspberry Pi by entering the following command `sudo raspi-config`. Go to Interfacing Options. Enable remote GPIO (optional: also enable SSH and VNC for remote control of your Pi). 
* Update your software by executing the following commands: `sudo apt-get update`, `sudo apt-get upgrade`.
* Install latest python3 version: `sudo apt-get install python3`. (required for the python application to run)
* Install lasest RPi.GPIO module for python3: `sudo apt-get install python3-rpi.gpio`.

2. Download source code on the Pi
* Installing Git: `sudo apt-get install git-core`
* clone this git repository: `git clone https://github.com/jeroennijhuis/RubiksCubeSolver.git`





