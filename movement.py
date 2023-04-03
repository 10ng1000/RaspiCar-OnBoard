import wheel
import RPi.GPIO as GPIO
import time


class Movement:
    def __init__(self):
        # 左前，右前，左后，右后
        #  pwm pin1 pin2
        # wheel1 = wheel.Wheel(17, 27, 22)
        # wheel2 = wheel.Wheel(24, 23, 25)
        # wheel3 = wheel.Wheel(26, 6, 5)
        # wheel4 = wheel.Wheel(16, 21, 20)
        self.wheel1 = wheel.Wheel(18, 14, 15)
        self.wheel2 = wheel.Wheel(11, 9, 10)
        self.wheel3 = wheel.Wheel(23, 25, 24)
        self.wheel4 = wheel.Wheel(13, 5, 6)
        self.shift_speed = 70
        self.rotate_speed = 40
        self.forward_speed = 50

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

    def left_rotate(self, t):
        self.set_speed([-self.rotate_speed, self.rotate_speed, -self.rotate_speed, self.rotate_speed])
        time.sleep(t)
        self.set_speed([0, 0, 0, 0])

    def right_rotate(self, t):
        self.set_speed([self.rotate_speed, -self.rotate_speed, self.rotate_speed, -self.rotate_speed])
        time.sleep(t)
        self.set_speed([0, 0, 0, 0])

    def left_shift(self, t):
        self.set_speed([-self.shift_speed, self.shift_speed, self.shift_speed, -self.shift_speed])
        time.sleep(t)
        self.set_speed([0, 0, 0, 0])

    def right_shift(self, t):
        self.set_speed([self.shift_speed, -self.shift_speed, -self.shift_speed, self.shift_speed])
        time.sleep(t)
        self.set_speed([0, 0, 0, 0])

    def back(self, t):
        self.set_speed([-self.forward_speed, -self.forward_speed, -self.forward_speed, -self.forward_speed])
        time.sleep(t)
        self.set_speed([0, 0, 0, 0])

    def forward(self, t):
        self.set_speed([self.forward_speed, self.forward_speed, self.forward_speed, self.forward_speed])
        time.sleep(t)
        self.set_speed([0, 0, 0, 0])

    def __del__(self):
        GPIO.cleanup()


if __name__ == '__main__':
    m = Movement()
    for i in range(10):
        j = i * 10
        m.set_speed([j, j, j, j])
        time.sleep(1)
