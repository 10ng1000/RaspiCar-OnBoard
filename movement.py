import wheel
import RPi.GPIO as GPIO
import time

class Movement:
    def __init__(self):
        # 左前，右前，左后，右后
        self.wheel1 = wheel.Wheel(22, 27, 17)
        self.wheel2 = wheel.Wheel(23, 24, 25)
        self.wheel3 = wheel.Wheel(5, 6, 13)
        self.wheel4 = wheel.Wheel(12, 16, 20)

    def set_speed(self, speed_list):
        self.wheel1.set_speed(speed_list[0])
        self.wheel2.set_speed(speed_list[1])
        self.wheel3.set_speed(speed_list[2])
        self.wheel4.set_speed(speed_list[3])

    def stop(self):
        self.wheel1.stop()
        self.wheel2.stop()
        self.wheel3.stop()
        self.wheel4.stop()

    def __del__(self):
        GPIO.cleanup()


GPIO.cleanup()
