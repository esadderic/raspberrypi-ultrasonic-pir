import RPi.GPIO as GPIO
import time

LED = 24
US_TRIG = 20
US_ECHO = 26

GPIO.setmode(GPIO.BCM)
# setup
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(US_TRIG, GPIO.OUT)
GPIO.setup(US_ECHO, GPIO.IN)


# controls
GPIO.output(LED, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(LED, GPIO.LOW)
print("US Sensor setaping")
GPIO.output(US_TRIG, False)
time.sleep(2)
print("Sensor finished")

last_result = None
last = False
while True:
    if last:
        GPIO.output(LED, GPIO.LOW)

    GPIO.output(US_TRIG, True)
    time.sleep(0.0001)
    GPIO.output(US_TRIG, False)
    while GPIO.input(US_ECHO) == 0:
        pulse_start = time.time()
    
    while GPIO.input(US_ECHO) == 1:
        pulse_end = time.time()
    

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 0)
    print("Distance: ",distance, " CM")
    time.sleep(1)
    
    
    if last_result == None:
        last_result = distance
    print("D",distance, "L", last_result)
    
    if distance != last_result:
        last = not last
        print("found")
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        last_result = distance
    


time.sleep(1)
#GPIO.output(24, GPIO.LOW)
#GPIO.cleanup()
GPIO.cleanup()
