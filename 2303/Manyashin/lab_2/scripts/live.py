import random
import rospy
import sys
from .msg import Signal 
from .repair import *
from random import random

crash_benzin = 0.1
crash_ruler = 0.01
crash_engine = 0.05

class Car:
    """
    Означает машину:
    Детали означаю вещи способные сломаться.

    """

    def __init__(self):
        self.engine = False
        self.ruler = False
        self.benzin = False
        self.alive = True
    
    def fix(self,name):
        self['name'] = False

    def run(self):
        pub = rospy.Publisher('dispatcher_car', Signal, queue_size=20)
        patient = rospy.Subscriber('dispatcher_repair', Signal, self.fix)
        rospy.init_node("livenode", anonymous=True)

        while(self.alive):
            
            if(random() < crash_benzin): 
                pub.publish("Crash benzin")
                self.benzin = True

            if(random() < crash_ruler): 
                pub.publish("Crash ruler")
                self.ruler = True

            if(random() < crash_engine): 
                pub.publish("Crash engine")
                self.engine = True

            if (self.engine and self.ruler and self.benzin):
                self.alive = False

        rospy.loginfo("\nCar is crached")
        rospy.signal_shutdown("FAILED")


def run():
    car = Car()
    car.run()


if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass