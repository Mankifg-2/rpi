#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LedPins = [17,27]

def setup():
    
    GPIO.setmode(GPIO.BCM)
    for led in LedPins:
        GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

def main():
    while True:
        print ('[+] ')
        on(0)
        off(1)
        time.sleep(0.5)
        print ('[-] ')
        on(1)
        off(0)
        time.sleep(0.5)

def on(i):
    GPIO.output(LedPins[i], GPIO.LOW)

def off(i):
    GPIO.output(LedPins[i], GPIO.HIGH)

def destroy():
    for led in LedPins:
        GPIO.output(led, GPIO.HIGH)
    GPIO.cleanup()                   


if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()