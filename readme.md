### AutoSteer 
AutoSteer leverages computer vision and Convolutional Neural Networks (CNNs) to predict high-precision steering angles for autonomous vehicles. This project aims to enhance road safety and driving efficiency through advanced AI technology.

### Dataset 
You can get the dataset at [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584f6edd_data/data.zip)

### Code Requirements 
Conda for Python which resolves all the dependencies for machine learning.

`pip install requirements.txt`

### Setup 

1) First, run `LoadData.py` which will get the dataset from the folder and store it in a pickle file.
2) Now you need to have the data, run `TrainModel.py` to load data from pickle and augment it. After this, the training process begins.
3) For testing it on the video, run `DriveApp.py`

### Results

<img src="https://github.com/akshaybahadur21/BLOB/blob/master/final.gif">
