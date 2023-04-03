from obstacleAvoidance import ObstacleAvoidance
import threading
from movement import Movement
import time


class AutoMoveWithObstacle:
    def __init__(self, obstacle_avoidance):
        self.on = False
        self.speed = 45
        self.obstacle_avoidance = obstacle_avoidance

    def start(self):
        self.on = True
        while self.on:
            if not self.obstacle_avoidance.is_encounter_obstacle():
                self.obstacle_avoidance.move_control.set_speed([self.speed, self.speed, self.speed, self.speed])
                time.sleep(0.5)
            else :
                self.obstacle_avoidance.move_control.stop()
                print('avoiding')
                time.sleep(5.0)
    def stop(self):
        print('automove stop called')
        self.on = False
        self.obstacle_avoidance.move_control.stop()

if __name__ == '__main__':
    ob = ObstacleAvoidance(Movement())
    threading.Thread(target= ob.start).start()
    am = AutoMoveWithObstacle(ob)
    threading.Thread(target= am.start).start()
