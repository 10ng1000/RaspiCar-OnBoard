import RPi.GPIO as GPIO
import time

# GPIO
in1 = 22
in2 = 27
en = 17
stby = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(stby, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 300)

p.start(0)

p.ChangeDutyCycle(100)
GPIO.output(stby, GPIO.HIGH)
GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)

time.sleep(5)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.cleanup()
