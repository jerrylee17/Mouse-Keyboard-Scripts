import pyautogui as pag
import time
from random import seed, random
import sys


# getMousePosition()
class owoHax:
    def __init__(self, position):
        self.position = position

    def writeText(self):
        # Move and click
        currpos = pag.position()
        pag.click(self.position)
        pag.typewrite("owoh")
        pag.typewrite(["enter"])
        pag.typewrite("owob")
        pag.typewrite(["enter"])
        pag.moveTo(currpos)

    def loopHax(self):
        time.sleep(1)
        for i in range(40):
            self.writeText()
            # generate random wait time between 15 and 30 seconds inclusive
            wait = int(15 + random()*16)
            print('Iteration number', i+1, '| waiting: ', wait, 'seconds')
            self.timer(wait)

    def timer(self, wait):
        for i in range(wait, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(i))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
