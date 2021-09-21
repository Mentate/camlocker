import cv2
import time
import win32api #seems like this is included with the windows python installer sometimes? I had to install it so I added it to the requirements.txt to be safe
import ctypes


#for some reason the lbp file didn't come with opencv and had to be downloaded. because of this I had to put the path in, which is gross
frontfaceCascade = cv2.CascadeClassifier(r'lbpcascade_frontalface.xml')


#there's no point in checking for facial presense if the keyboard and mouse are being used.
#this returns seconds since last input
def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0

#this checks for a face. If no face is found it checks once a second for five seconds
# If no faces are found during the entire 5 seconds it returns False. If it finds a face it returns True
def checkcam():
    #we don't want to capture the camera all the time. That would lock other apps out of it
    cap = cv2.VideoCapture(0)
    
    #if another app has control of the camera, base image will be None.
    #That means the user is using the webcam for another app and we probably shouldn't lock the machine anyways
    rc, baseImage = cap.read()
    try:
        #if the base image is none the line below throws an error. This is how we know the webcam is being used by something else
        gray = cv2.cvtColor(baseImage,cv2.COLOR_BGR2GRAY)      
    except:        
        cap.release()
        return True
    frontfaces = frontfaceCascade.detectMultiScale(gray,1.05,2)
    if(len(frontfaces) == 0):
        i = 0
        
        for x in range(5):
            time.sleep(1)
            rc, baseImage = cap.read()
            gray = cv2.cvtColor(baseImage,cv2.COLOR_BGR2GRAY)
            frontfaces = frontfaceCascade.detectMultiScale(gray,1.05,4)
            if(len(frontfaces) == 0):
                i = i +1
        if(i == 5):
            cap.release()
            return False
            
        else:   
            cap.release()
            return True
    else:
        cap.release()
        return True


while True:
    #we don't need this running constantly. Check every 6 seconds
    time.sleep(6)
    idletime = getIdleTime()
    if(idletime > 5):#if the machine has been  idle check for faces
        face = checkcam()
        if(face == False):
            #If we get here then there has been no input or faces for 5 seconds
            #time to lock the machine
            print("no face")
            ctypes.windll.user32.LockWorkStation()
            #there's no point in running while the machine is locked
            #this checks if it's locked every 3 seconds.
            #Once the machine is unlocked it waits 30 seconds to resume function
            #this is a failsafe so the code doesn't instantly lock the machine if 
            #something goes wrong with the code
            while(ctypes.windll.user32.GetForegroundWindow() == 0):
                time.sleep(3)
            else:
                time.sleep(30)


    