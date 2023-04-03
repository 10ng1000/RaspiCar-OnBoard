import RPi.GPIO as GPIO
import time

# GPIO
in1 = 27
in2 = 17
en = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 100)

p.start(0)

p.ChangeDutyCycle(50)
GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)

time.sleep(2)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.cleanup()
