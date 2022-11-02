import gpio
import time

# GPIO
# 具体控制方法在客户端中实现
class Wheel:
    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)


    def set_speed(self, speed_list):
        GPIO.output(self.pin1, speed_list[0])
        GPIO.output(self.pin2, speed_list[1])
        GPIO.output(self.pin3, speed_list[2])
        GPIO.output(self.pin4, speed_list[3])


