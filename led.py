#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LedPin = 17

def setup():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

def main():
    while True:
        print ('[+] ', end=", ")
        # Turn on LED
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(0.5)
        print ('[-] ',end=", ")
        # Turn off LED
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.5)


def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()                   


if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()