from autoOwo import owoHax
import pyautogui as pag
import time

# Get mouse position


def getMousePosition():
    while True:
        time.sleep(1)
        print(pag.position())


# getMousePosition()

position = (2595, 1042)
hax = owoHax(position)
hax.loopHax()
