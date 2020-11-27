#!/usr/bin/env python

#Minimize window


import ctypes
from win10toast import ToastNotifier 

import os
import sys
from time import sleep
import autopy

backuppath = "C:\\Backupcake"
desktoppath = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'))

def createbackupfolder():
	folder_name = "Backupcake"
	folder_path = "C:\\" + folder_name
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		print("Successfully created folder ", folder_name)

	elif os.path.exists(folder_path):
		print(folder_path, " Already exists")
	else:
		sys.exit()

def movedesktopfiles():

	files = os.listdir(desktoppath)
	number_files = len(files)
	print("There is " + str(number_files) + " files on desktop")
	print("____________________________________")


	for file in os.listdir(desktoppath):
		try:
			print("{0:<30} {1:<10}".format(file, "Have been moved to " + backuppath))
			os.rename(desktoppath + "\\" + file, backuppath + "\\" + file)
		except Exception as e:
			print(e)

def takensavescreenshot():

	bitmap = autopy.bitmap.capture_screen()
	bitmap.save("C:\\Backupcake\\screenshot.png")


def changebackground():
	ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Backupcake\\screenshot.png" , 0)
def main():


	
	createbackupfolder()
	print()
	sleep(5)
	takensavescreenshot()
	print()
	movedesktopfiles()
	print()
	changebackground()


	toaster= ToastNotifier()
	toaster.show_toast("Fakecake","VIktor can suck a ass")


	sys.exit()
	
	

if __name__ == '__main__':
	main()