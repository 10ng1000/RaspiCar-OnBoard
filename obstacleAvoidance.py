import threading
import time

import hcsr04
import sg90
import movement

class ObstacleAvoidance:
    def __init__(self, move_control):
        self.dis = 20
        self.move_control = move_control
        self.sg90 = sg90.Sg90()
        self.hcsr04 = hcsr04.Hcsr04()
        self.on = False
        self.is_obstacle = False

    def run(self):
        self.is_obstacle = False
        front = self.hcsr04.get_distance()
        if front > self.dis:
            return
        self.is_obstacle = True
        self.sg90.serve(self.sg90.LEFT)
        time.sleep(1)
        left = self.hcsr04.get_distance()
        self.sg90.serve(self.sg90.RIGHT)
        time.sleep(1.7)
        right = self.hcsr04.get_distance()
        self.sg90.serve(self.sg90.MID)
        print(str(left) + ',' + str(right))
        if (left < 0.5 * self.dis and right < 0.5 * self.dis) or front < 0.5 * self.dis:
            self.move_control.back(1.5)
        elif left > right:
            self.move_control.left_shift(1)
        else :
            self.move_control.right_shift(1)

    def start(self):
        if self.on:
            print('return')
            return
        self.on = True
        while self.on:
            self.run()
            time.sleep(0.1)

    def stop(self):
        print('stop called')
        self.on = False

    def is_encounter_obstacle(self):
        return self.is_obstacle

if __name__ == '__main__' :
    m = movement.Movement()
    ob = ObstacleAvoidance(m)
    l = threading.Thread(target= ob.start)
    l.start()
    s = input("input s to stop")
    print(s)
    if s == 's':
        print('stop')
        ob.stop()
