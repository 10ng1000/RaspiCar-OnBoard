import time
from movement import Movement
from obstacleAvoidance import ObstacleAvoidance


class CircularMovement:
    def __init__(self, obstacle_avoidance):
        self.width = 14
        self.length = 12
        self.bend_k = 3
        self.axle_k = 1.6
        self.obstacle_avoidance = obstacle_avoidance
        self.move_control = obstacle_avoidance.move_control

    # 参数v表示的是线速度，基准速度为50
    def start(self,  side):
        v = 0
        hcsr = self.obstacle_avoidance.hcsr04
        sg = self.obstacle_avoidance.sg90
        if side == 'bend':
            sg.serve(sg.RIGHT)
        time.sleep(1)
        r = hcsr.get_distance()
        if side == 'axle':
            r = r + self.length / 2 + 10
        print(r)
        if side == 'bend':
            v = 50
            v_out = v + self.width / 2 * v / r * self.bend_k
            v_in = v - self.width / 2 * v / r * self.bend_k
        elif side == 'axle':
            v = 70
            v_out = v + self.length / 2 * v / r * self.axle_k
            v_in = v - self.length / 2 * v / r * self.axle_k
        print(v_out)
        print(v_in)
        if side == 'bend':
            self.move_control.back(1)
        elif side == 'axle':
            self.move_control.right_shift(1)
        self.move_control.stop()
        time.sleep(0.5)
        if side == 'bend':
            self.move_control.forward(1.45)
        elif side == 'axle':
            self.move_control.left_shift(1)
        t = 200
        while t > 0:
            if side == 'bend':
                self.move_control.set_speed([v_out, v_in, v_out, v_in])
            elif side == 'axle':
                self.move_control.set_speed([-v_in, v_in, v_out, -v_out])
            t = t - 1
            time.sleep(0.1)
        time.sleep(0.5)
        sg.serve(sg.MID)

if __name__ == '__main__':
    m = Movement()
    ob = ObstacleAvoidance(m)
    c = CircularMovement(ob)
    c.start('axle')

