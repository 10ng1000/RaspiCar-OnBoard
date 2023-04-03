import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Sg90:

    def __init__(self):
        self.pin1 = 16
        self.FRE = 50
        self.LEFT = 11
        self.RIGHT = 2
        self.MID = 7
        GPIO.setup(16, GPIO.OUT)
        self.servo1 = GPIO.PWM(self.pin1, self.FRE)
        self.servo1.start(0)

    def serve(self, pwm):
        self.servo1.ChangeDutyCycle(pwm)
        time.sleep(0.2)
        self.servo1.ChangeDutyCycle(0)

    def __del__(self):
        self.servo1.stop()
        GPIO.cleanup()
