from autoOwo import owoHax
import pyautogui as pag
import time

# Get mouse position
def getMousePosition():
    while True:
        time.sleep(1)
        print(pag.position())

position = (-1498, 784)
hax = owoHax(position)
hax.loopHax()

