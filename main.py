import sys
import time
from grove.factory import Factory

print("starting")

from grove.helper import SlotHelper
sh = SlotHelper(SlotHelper.ADC)
pin = sh.argv2pin()

sensor = Factory.getTemper("NTC-ADC", pin)

print('Detecting temperature...')
while True:
    print('{} Celsius'.format(sensor.temperature))
    time.sleep(1)
