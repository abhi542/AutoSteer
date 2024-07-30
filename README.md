## Description 🏎️
An autonomous car (also known as a driverless car, self-driving car, and robotic car) is a vehicle that is capable of sensing its environment and navigating without human input. Autonomous cars combine various techniques to perceive their surroundings, including radar, laser light, GPS, odometry, and computer vision. Advanced control systems interpret sensory information to identify appropriate navigation paths, as well as obstacles and relevant signage

### Dataset 🗃️
You can get the dataset at [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip)

## Code Requirements 🦄
Conda for Python which resolves all the dependencies for machine learning.

`pip install requirements.txt`

### Setup 🖥️

1) First, run `LoadData.py` which will get dataset from folder and store it in a pickle file.
2) Now you need to have the data, run `TrainModel.py` to load data from pickle and augment it. After this, the training process begins.
3) For testing it on the video, run `DriveApp.py`

### Results 📊

<img src="https://github.com/akshaybahadur21/BLOB/blob/master/final.gif">
