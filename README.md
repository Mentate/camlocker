# CamLocker

## What it is
I work in cyber security, and everyone loves to pwn each other when we make the mistake of walking away from our machines without locking them. 
Even the most security conscience people make the mistake sometimes, so this is a safety net to help out with that.

## What it does
This is a simple python app. Every 5 seconds it checks how long it's been since there has been keyboard/mouse input. If it's been more than 6 seconds (this is adjustable) then it access the web cam and uses openCV for facial detection. If it finds a face, it loops back to checking for input every 5 seconds. If not, It continues to check for another 5 seconds (also adjustable) If it doesn't see a face for 5 seconds straight it will  lock the machine.
With this app running you can walk away from your machine and it should lock within 10 seconds of walking away.

## Caveats
If another app is using the web cam then the script will assume the computer is being used and will not lock it. As soon as the camera becomes available it will go back to checking for faces if no keyboard/mouse input is found
This app tries to tie up the camera as little as possible. In theory it is possible for the script to be using the camera when you try to start another app that uses it. If this happens just wait a few seconds and try again, it should work. Assuming you are actually using the keyboard/mouse before you start trying to use the camera this isn't very unlikely to happen


## Improvements
It would be great if this ran in the background instead of requiring an ugly console window to be up at all times. 
It would also be nice to have an icon in the task bar that lets you turn off or pause the application.
There are several values that can be customized (timers and parameters that effect facial detection sensitivity). A gui window to customize these would be helpful
Instalation would be hard for non-programmers. Having some kind of easy to install package would make this accessable to more users

## Contact
Pull requests are welcome.Feel free to contact me if needed: Josiah@JosiahCarpenter.com


