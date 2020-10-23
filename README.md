# Deptherm Inspection 

## Description

deptherm Inspection is a 3D thermographic inspection application and it's also an application for rgb, depth and thermal camera intrinsic
and extrinsic calibration. 


## Dependecies
* Ubuntu +18.04
* [QT](https://doc.qt.io/QtForAutomation/qtautomation-install.html)
* [libfreenect](https://github.com/OpenKinect/libfreenect)
* Python +3.7

After downloading the dependencies, run the following commands:
``` 
    sudo apt-get update -y

    sudo apt-get install -y python-freenect
```

This project needs **[libfreenect](https://github.com/OpenKinect/libfreenect)** on your computer to enter the microsoft kinect camera. If you are using a different camera you need to modify the file **src/acquisition/DataAcquisition.py** and ready, you can use this application.


## Project Setup
```
    git clone https://github.com/Jjat00/Deptherm-Inspection.git
```
```
    pip install -r requirements.txt
```

## Run Project
```
    python3.7 src/app.py
```


## More Informatation
Information about the OpenKinect project can be found at http://www.openkinect.org