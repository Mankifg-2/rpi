import RPi.GPIO as GPIO
import time


LedPin = 17



GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)


while True:
    try:
        print ('[+]', end=", ")

        GPIO.output(LedPin, GPIO.LOW)
        
        time.sleep(0.5)
        print ('[-]', end=", ")
        GPIO.output(LedPin, GPIO.HIGH)

        time.sleep(0.5)
        
    except KeyboardInterrupt:
        GPIO.output(LedPin, GPIO.HIGH)
        GPIO.cleanup()                   
