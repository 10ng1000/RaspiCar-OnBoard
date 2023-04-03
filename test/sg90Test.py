import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT )
servo1 = GPIO.PWM(16, 50)
servo1.start(0)
print("wait 2 sec")
time.sleep(2)
duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1

time.sleep(2)
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo1.stop()
GPIO.cleanup()
