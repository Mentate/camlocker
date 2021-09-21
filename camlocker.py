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
    #we don't want to capture the camera all the time. That would lock other apps out of it.
    #we only capture it when we need to check for a face
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)     
    for x in range(5): 
        time.sleep(1) #this is here so we only check once every second
        rc, baseImage = cap.read() #get an image
        try:
        #if the base image is none the line below throws an error. This is how we know the webcam is being used by something else
            gray = cv2.cvtColor(baseImage,cv2.COLOR_BGR2GRAY)      
        except:        
            cap.release()
            cv2.destroyAllWindows()
            return True # if we get here the webcam is in use by another app. Return true since we assume the machine is being used
        frontfaces = frontfaceCascade.detectMultiScale(gray,1.05,4)
        if(len(frontfaces) != 0):
            cap.release()
            cv2.destroyAllWindows()
            return True #if we find a face we imediatly return true
            
    cap.release() #release the camera for other apps to use it
    cv2.destroyAllWindows()
    return False #we can only get here if no faces were found in the for loop, so we need to return false



while True:
    #we don't need this running constantly. Check every 5 seconds
    time.sleep(5)
    idletime = getIdleTime()
    if(idletime > 5):#if the machine has been  idle check for faces
        face = checkcam()
        if(face == False):
            #the machine has been idle and there have been no faces found. time to lock
            print("no face")
            ctypes.windll.user32.LockWorkStation()
            #there's no point in running while the machine is locked
            #this checks if it's locked every 3 seconds.
            #Once the machine is unlocked it waits 30 seconds to resume function
            #this is a failsafe so the code doesn't instantly lock the machine if 
            #something goes wrong with the code
            while(ctypes.windll.user32.GetForegroundWindow() == 0):
                time.sleep(3)            
            
            time.sleep(30)


    