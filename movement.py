import wheel
import RPi.GPIO as GPIO
import time

class Movement:
    def __init__(self):
        # 左前，右前，左后，右后
        # wheel1 = wheel.Wheel(17, 27, 22)
        # wheel2 = wheel.Wheel(24, 23, 25)
        # wheel3 = wheel.Wheel(26, 6, 5)
        # wheel4 = wheel.Wheel(16, 21, 20)
        self.wheel1 = wheel.Wheel(17, 27, 22)
        self.wheel2 = wheel.Wheel(24, 23, 25)
        self.wheel3 = wheel.Wheel(26, 6, 5)
        self.wheel4 = wheel.Wheel(16, 21, 20)

    def set_speed(self, speed_list):
        self.wheel1.set_speed(speed_list[0])
        self.wheel2.set_speed(speed_list[1])
        self.wheel3.set_speed(speed_list[2])
        self.wheel4.set_speed(speed_list[3])

    def left(self):
        self.set_speed([100, 50, 50, 100])
        time.sleep(0.5)
        self.stop()

    def right(self):
        self.set_speed([50, 100, 100, 50])
        time.sleep(0.5)
        self.stop()

    def stop(self):
        self.wheel1.stop()
        self.wheel2.stop()
        self.wheel3.stop()
        self.wheel4.stop()

    def __del__(self):
        GPIO.cleanup()