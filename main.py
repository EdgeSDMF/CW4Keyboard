import RPi.GPIO as GPIO
import time

CW_PIN = 17  # GPIO pin connected to the key line
WPM = 20     # words per minute

# Calculate dot duration
DOT_DURATION = 1.2 / WPM

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': ' '
}

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CW_PIN, GPIO.OUT)
    GPIO.output(CW_PIN, GPIO.LOW)

def key_down():
    GPIO.output(CW_PIN, GPIO.HIGH)

def key_up():
    GPIO.output(CW_PIN, GPIO.LOW)

def send_symbol(symbol):
    if symbol == '.':
        key_down()
        time.sleep(DOT_DURATION)
    elif symbol == '-':
        key_down()
        time.sleep(DOT_DURATION * 3)
    key_up()
    time.sleep(DOT_DURATION)  # space between parts of the same letter

def send_char(char):
    for symbol in MORSE_CODE_DICT.get(char.upper(), ''):
        send_symbol(symbol)
    time.sleep(DOT_DURATION * 2)  # space between characters

def main():
    setup()
    try:
        while True:
            text = input("Enter text: ")
            for char in text:
                send_char(char)
            print("Done sending.")
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
