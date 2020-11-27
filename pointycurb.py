import random
import win32.win32api as winapi
import pyautogui
import winsound
import os

state_left = winapi.GetKeyState(0x01) 

def getclick(click):
    if click < 0:
        return True
    return False


def main():
    while True:
        try:
            a = winapi.GetKeyState(0x01)
            #Manage click
            if getclick(a):
                winsound.Beep(40,50)
                clickposition = pyautogui.position()
                rX = 0
                rY = 0
                while rX == 0 or rY == 0:
                    rX = random.randint(-300,300)
                    rY = random.randint(-300,300)

                    X = clickposition[0] % rX
                    Y = clickposition[1] % rY
                print(f"{clickposition} : {X} {Y}")
                pyautogui.move(X,Y)
        except:
            pass

if __name__ == "__main__":
    os.system("cls")
    main()
