import cv2
import os
import numpy as np
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
i=-1
imagepaths= getListOfFiles("C:\\Users\\Yashobam\\Downloads\\6\\2")
timg=len(imagepaths)
def next(i,imagepaths):
	i+=1
	if imagepaths[i].endswith("png") or imagepaths[i].endswith("jpg") or imagepaths[i].endswith("JPG") :
		showimage(i,imagepaths)
	elif imagepaths[i].endswith("MP4"):
		showvideo(i,imagepaths)
	else:
		next(i,imagepaths)
def back(i,imagepaths):
	i-=1
	if imagepaths[i].endswith("png") or imagepaths[i].endswith("jpg") or imagepaths[i].endswith("JPG") :
		showimage(i,imagepaths)
	elif imagepaths[i].endswith("MP4"):
		showvideo(i,imagepaths)
	else:
		back(i,imagepaths)
def update(i,imagepaths):
	imagepaths=getListOfFiles("C:\\Users\\Yashobam\\Downloads\\6\\2")
	i-=1
def removes(i,imagepaths):
	for j in range(len(imagepaths[i])-1,0,-1):
		if imagepaths[i][j]=="\\":
			j+=1
			imagename=imagepaths[i][j:]
			break
	os.rename(imagepaths[i],"C:\\Users\\Yashobam\\Downloads\\6\\removed\\{}".format(imagename))
	update(i,imagepaths)
def undo(i,imagepaths):
	for j in range(len(imagepaths[i-1])-1,0,-1):
		if imagepaths[i-1][j]=="\\":
			j+=1
			imagename=imagepaths[i-1][j:]
			break

	os.rename("C:\\Users\\Yashobam\\Downloads\\6\\removed\\{}".format(imagename),imagepaths[i-1])
	update(i,imagepaths)
def showimage(i,imagepaths):
	while True:
		print(imagepaths[i]+str(i+1)+"/"+str(timg))
		image=cv2.imread(imagepaths[i])
		h, w, c = image.shape
		scale=500/h
		width=int(w*scale)
		resized = cv2.resize(image, (width,500), interpolation = cv2.INTER_AREA)
		cv2.imshow("Image",resized)
		key = cv2.waitKey(0)
		if key == ord('1'):
			removes(i,imagepaths)
			update(i,imagepaths)
			next(i,imagepaths)
		if key == ord("2"):
			next(i,imagepaths)
		if key == ord('3'):
			update(i,imagepaths)
			undo(i,imagepaths)
			i-=1
			showimage(i,imagepaths)
		if key==ord("4"):
			back(i,imagepaths)
		if key==ord("5"):
			q=open("temp.txt","w", encoding="utf-8")
			q.write(str(i))
			cv2.destroyAllWindows()

def showvideo(i,imagepaths):
	while True:
		print(imagepaths[i]+str(i+1)+"/"+str(timg))
		cap=cv2.VideoCapture(imagepaths[i])
		while cap.isOpened()==True:
			ret, frame = cap.read()
			if cap.read()[0]!=False:
				h, w, c = frame.shape
				scale=500/h
				width=int(w*scale)
				resized = cv2.resize(frame, (width,500), interpolation = cv2.INTER_AREA)
				cv2.imshow("Image",resized)
				key = cv2.waitKey(1)
				if key == ord('1'):
					removes(i,imagepaths)
					next(i,imagepaths)
				if key == ord("2"):
					next(i,imagepaths)
				if key == ord('3'):
					undo(i,imagepaths)
					i-=1
					showimage(i,imagepaths)
				if key==ord("4"):
					back(i,imagepaths)
				if key==ord("5"):
					q=open("temp.txt","w", encoding="utf-8")
					q.write(str(i))
					cv2.destroyAllWindows()
			else:
				showvideo(i,imagepaths)
def start(i,imagepaths):
	q=open("temp.txt","r", encoding="utf-8")
	
	x=input("Do you want to continue from "+str(q.read())+"[y/n]")
	if x.lower()=="y":
		print(q.read())
		next(q.read(),imagepaths)
	else:
		next(-1,imagepaths)
start(i,imagepaths)
cv2.destroyAllWindows() 