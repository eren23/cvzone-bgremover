# Virtual BG for Linux Zoom Users

Basic functionality works properly at the moment, before running the code check existing camera devices with the command: ls /dev | grep -P '^video\d+$'

Then you can create the fakewebcam device using the instructions [here](https://github.com/jremmons/pyfakewebcam), when you rerun the code above you should see the new devices.

Todo:
Making it a bit more dynamic
GUI
Selecting Images Through GUI
