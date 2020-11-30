import ctypes
from ctypes import wintypes
import sys
user32 = ctypes.WinDLL("user32")

SW_HIDE = 0
SW_SHOW = 5

user32.FindWindowW.restype = wintypes.HWND
user32.FindWindowW.argtypes = (
    wintypes.LPCWSTR, # lpClassName
    wintypes.LPCWSTR) # lpWindowName

user32.ShowWindow.argtypes = (
    wintypes.HWND, # hWnd
    ctypes.c_int)  # nCmdShow

def lock_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_HIDE)

def unlock_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_SHOW)

if __name__ == "__main__":
    if '-l' in sys.argv:
        lock_taskbar()
    elif '-ul' in sys.argv:
        unlock_taskbar()
    else:
        print("COMMANDS")
        print("-l | Lock taskbar")
        print("-ul | unLock taskbar")
