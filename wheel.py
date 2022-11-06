import RPi.GPIO as GPIO
import time

# GPIO
class Wheel:
    def __init__(self, en, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        self.en = en
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        self.p = GPIO.PWM(self.en, 1000)
        self.p.start(0)


    def set_speed(self, speed):
        self.p.ChangeDutyCycle(speed)
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)


