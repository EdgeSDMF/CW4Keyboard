# CW4Keyboard 4 Raspberry Pi / GPIO
Keyboard to CW for HF Radio
# CW Keyboard to HF Radio Keyer Raspberry Pi / GPIO

This project allows you to type Morse code (CW) using your keyboard, transmitting it via GPIO to an HF radio, effectively replacing a manual key or paddle [[2](https://www.reddit.com/r/amateurradio/comments/1he9ahv/cw_key_and_keyer_combo/)].

## Features
- Converts keyboard input into Morse code
- Sends dits/dahs via GPIO (e.g. Raspberry Pi)
- Adjustable WPM

## Requirements
- Raspberry Pi (or compatible GPIO platform)
- Python 3
- RPi.GPIO module

## Setup
```bash
pip install RPi.GPIO
python3 main.py
