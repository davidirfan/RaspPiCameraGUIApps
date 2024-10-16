# RaspPiCameraGUIApps
I am still working on the development of a simple GUI Application for using Raspberry Pi Camera to take photos and record videos. There are some problem i still encounter.

## Objective
- To develop an executable application on Raspberry Pi OS to using camera for take photos and record videos without need to using Python IDE and Terminal to run the program

Requirement :
For this development, i use :
1. Raspberry Pi 4 with Raspberry Pi OS Version No. 11 Bullseye
2. Raspberry Pi Camera from ArduCam 16MP IMX519 and its software installation
3. Python and its IDE
4. Python library : TKInter

There are 4 python program files in this repository. Each program has different function.
## PreviewWindowRaspPiCamera.py
This Python program files is use to open the window of preview camera.
How to use it :
1. Before run the program, make sure you already able to use the camera of Raspberry Pi.
2. Open the program file using your Python IDE and run it.
3. The window of preview camera will open like this example below.
![GUI Window of Preview Camera](https://github.com/davidirfan/RaspPiCameraGUIApps/blob/main/Gallery/TryPreviewCamera.PNG)
4. To close the window, click x button.

## TakePhotoWindowRaspberryPiCamera.py 
This Python program files is use to open the window of preview camera and take photos.
How to use it :
1. Before run the program, make sure you already able to use the camera of Raspberry Pi.
2. Open the program file using your Python IDE and run it.
3. The window of preview camera will open like this example below.
4. There is a button "Take Photo" below to take photos. Click that button and the photos will capture and save on the new folder named "photo" that still inside Python program folder.
![GUI Window of Preview Camera and Take Photos](https://github.com/davidirfan/RaspPiCameraGUIApps/blob/main/Gallery/Preview%26TakePhotos.PNG)
5. To close the window, click x button.

## RecordVideoWindowRaspberryPiCamera.py
This Python program files is use to open the window of preview camera and record videos.
How to use it :
1. Before run the program, make sure you already able to use the camera of Raspberry Pi.
2. Open the program file using your Python IDE and run it.
3. The window of preview camera will open like this example below.
4. There are two button below, "Start Recording" to start the record video and "Stop Recording" to stop the record. The video will be saved after Stop button clicked. Video saved as h.264 format on the new folder named "video" that still inside Python program folder.
![GUI Window of Preview Camera and Take Photos](https://github.com/davidirfan/RaspPiCameraGUIApps/blob/main/Gallery/Preview%26RecordVideos.PNG)
5. To close the window, click x button.

## TakePhotos&VideosWindowRaspberryPiCamera.py 
This Python program files is use to open the window of preview camera, take photos, and record videos.
How to use it :
1. Before run the program, make sure you already able to use the camera of Raspberry Pi.
2. Open the program file using your Python IDE and run it.
3. The window of preview camera will open like this example below.
4. There are buttons.
![GUI Window of Preview Camera and Take Photos](https://github.com/davidirfan/RaspPiCameraGUIApps/blob/main/Gallery/PreviewTakePhotosRecordVideos.PNG)
5. To close the window, click x button.

## PROBLEM
To open those GUI Raspberry Pi Camera program, you should open the python program first using IDE and run it. I want to convert those program to executable application to can run from the dekstop of Raspberry Pi OS without using IDE anymore.
