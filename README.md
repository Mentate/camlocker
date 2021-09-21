# CamLocker

## What it is
I work in cyber security, and everyone loves to pwn each other when we make the mistake of walking away from our machines without locking them. 
Even the most security conscience people make the mistake sometimes, so this is a safety net to help out with that.

## What it does
This is a simple python app. Every 5 seconds it checks how long it's been since there has been keyboard/mouse input. If it's been more than 6 seconds (this is adjustable) then it access the web cam and uses openCV for facial detection. If it finds a face, it loops back to checking for input every 5 seconds. If not, It continues to check for faces once a second for 5 seconds (also adjustable). If it doesn't see any faces in that 5 second duration it will lock the machine.
With this app running you can walk away from your machine and it should lock within about 10 seconds of walking away.

## Caveats
If another app is using the web cam then the script will assume the computer is being used and will not lock it. As soon as the camera becomes available it will go normal operation. This app tries to tie up the camera as little as possible, but in theory it is possible for the script to be using the camera when you try to start another app that uses the camera. If this happens just wait a few seconds and try again, it should work. Assuming you are actually using the keyboard/mouse before you start trying to use the camera this isn't very unlikely to happen.
Another issues is that the facial detection doesn't work well when the camera has a profile view instead of a frontal view of the face. This means if you turn your face completely perpendicular to the camera and aren't entering any input it could lock even though you are still in front of your desk. If this becomes a problem I would advize increasing the time that it checks for a face before locking. You could also adjust the sensitivity of the facial detection.


## Improvements
* It would be great if this ran in the background instead of requiring an ugly console window to be up at all times. 
* It would also be nice to have an icon in the task bar that lets you turn off or pause the application.
* There are several values that can be customized (timers and parameters that effect facial detection sensitivity). A gui window to customize these would be helpful
* Instalation would be hard for non-programmers. Having some kind of easy to install package would make this accessable to more users

## Contact
Pull requests are welcome.Feel free to contact me if needed: Josiah@JosiahCarpenter.com


