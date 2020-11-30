import pyautogui
import random
import winsound
import os
import shutil
from time import sleep as s
pyautogui.FAILSAFE = False
PROGRAMNAME = "Local Client Process.exe"
def knock(currmouseX, currmouseY):
    sleeptime = random.randint(5,10)
    winsound.Beep(1000,100)
    rX = 0
    rY = 0
    while rX == 0 or rY == 0:
        rX = random.randint(-500, 500)
        rY = random.randint(-500, 500)

    X = currmouseX % rX
    Y = currmouseY % rY
    print(f"{rX} {rY} : {X} {Y}")
    pyautogui.dragRel(X,Y)
    pyautogui.doubleClick()
    s(sleeptime)


def main():
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        print(str(currentMouseX) + " " + str(currentMouseY))
        knock(currentMouseX, currentMouseY)

if __name__ == "__main__":
    main()