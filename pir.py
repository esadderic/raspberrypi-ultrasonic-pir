
import RPi.GPIO as GPIO
import time

LED = 3
PIR = 11

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

# setup
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, GPIO.HIGH)
time.sleep(1)
GPIO.output(LED, GPIO.LOW)

i = 0
while True:
    res = GPIO.input(PIR)
    print(time.time(),res)
    time.sleep(1)
    

GPIO.cleanup()