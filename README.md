# midi2hid
Turn a MIDI controller into a mouse and keyboard (USB HID) using Arduino Yun

This code turns a Launchpad S from Ableton into a USB HID device by emulating both a mouse and keyboard. The mappings can get used to play "WASD and mouse" based games (most first=person games on PC). The MIDI mappings could get easily modified to work with any MIDI controller and game.

## Preparing your Arduino Yun
- Install latest OpenWRT (OpenWrt-Yun 1.5.3) via https://www.arduino.cc/en/Main/Software
- Setup WLAN, insert SD Card and expand disk with the DiskSpaceExpander sketch (https://www.arduino.cc/en/Tutorial/ExpandingYunDiskSpace)
- Restart and wait until the white USB LED is on (indicates Linux boot completed)
- Connect via SSH (e.g. via Putty)
- Run the following commands
```
opkg update

// install pip and pyserial
opkg install distribute  
opkg install python-openssl  
easy_install pip 
pip install pyserial

// install soundcard and alsa utils
opkg install kmod-sound-core
opkg install kmod-usb-audio
opkg install alsa-utils
opkg install alsa-utils-seq
```

- Install the midi2hid.ino sketch via Arduino IDE 
- Transfer midi2hid.py to the YUN (e.g. via WinSCP)
- Un-power the YUN
- Plug your MIDI controller into the USB port
- Plug the YUN into the computer you want to control via HID using the micro-USB port
- Re-power the YUN and wait for the white USB light to come on again
- Connect via SSH (e.g. via Putty) and run ``` python midi2hid.py ```



