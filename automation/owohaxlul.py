import pyautogui as pag
import time

# print(pag.size())
# Get mouse position
def getMousePosition():
    while True:
        time.sleep(1)
        print(pag.position())

# getMousePosition()

# Discord text box is: Point(x=-1498, y=784)
# owo hunt/battle 15 second cooldown

def owoHax():
    # Move and click
    # pag.moveTo(-1498, 784)
    pag.click(-1498, 784)
    pag.typewrite("owoh")
    pag.typewrite(["enter"])
    pag.typewrite("owob")
    pag.typewrite(["enter"])

def loopHax():
    for i in range(40):
        owoHax()
        print('Iteration number ', i+1)
        time.sleep(30)

time.sleep(1)
loopHax()