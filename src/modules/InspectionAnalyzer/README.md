# 3D Thermal Inspection Analyzer

## Description

3D thermal inspection analyzer is an application that allows you to capture data from rgb, depth and thermal images, it transforms this information to a point cloud with color or temperature to make a thermographic inspection analysis. It also allows to apply some filters both in the images and in the point cloud, it is possible to make simple captures of a single point cloud or to make an alignment of a group of point cloud with the ICP algorithm.

# Dependencies

* Ubuntu +18.04
* libfreenect
* Python +3.7

After downloading the dependencies, run the following commands:

```
    sudo apt-get update -y

    sudo apt-get install -y python-freenect
```

This project needs libfreenect on your computer to enter the microsoft kinect camera. If you are using a different camera you need to modify the file DataAcquisition.py and ready, you can use this application.

# Project Setup

```
git clone https://github.com/Jjat00/3D-Thermal-Inspection-Analyzer.git

pip install -r requirements.txt
```

# Run Project

python3.7 src/InspectionAnalizerApp.py
