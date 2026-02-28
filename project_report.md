# AutoSteer: Autonomous Driving Project Report

## 1. Project Overview
AutoSteer is an autonomous driving project that uses computer vision and Convolutional Neural Networks (CNNs) to predict steering angles from dashcam video feeds. By mimicking human driving behavior recorded in a dataset, the model learns to output high-precision steering angles to autonomously navigate a vehicle.

## 2. Dataset and Preprocessing
The model learns from the **Udacity Driving Dataset**, which contains:
- Center, Left, and Right camera images.
- Steering wheel angles corresponding to each frame.

**Preprocessing Steps:**
- Images are converted from RGB to the HSV color space, specifically isolating the Saturation (S) channel to better detect lane markings and road features regardless of lighting.
- Images are resized (e.g., to 40x40 or 100x100 depending on the model version) to reduce computational load.
- Data augmentation is applied, including horizontally flipping images and negating the corresponding steering angles to balance the dataset.

## 3. Architecture Deep Dive
The project consists of two main iterations of the steering model:

### 3.1 Version 1 (`Autopilot/`)
- **Input:** 40x40 grayscale/saturation images.
- **CNN Architecture:**
  - 3 Convolutional layers (32, 64, 128 filters) with ReLU activation and MaxPooling.
  - Dropout layer (0.5) to prevent overfitting.
  - 3 Dense layers (128, 64, 1) to output a single steering angle.
- **Focus:** Optimized for pure speed and simplicity, making it efficient to train on standard CPUs.

### 3.2 Version 2 (`Autopilot_V2/`)
- **Input:** 100x100 grayscale/saturation images.
- **CNN Architecture:**
  - 6 Convolutional layers (arranged in blocks of two: 32, 64, 128 filters) with ReLU activation and MaxPooling.
  - Dropout layer (0.5).
  - 4 Dense layers (1024, 256, 64, 1).
- **Focus:** Built for more complex track generalization. The higher resolution and deeper network allow it to capture finer visual details like lane boundaries and curvatures.

## 4. Execution & Usage Guide

### Prerequisites
- Python 3.10 environment with `keras==2.15.0`, `tensorflow==2.15.0`, `opencv-python`, etc.
- Unzip the dataset into the `driving_dataset/` directory.

### Running Version 1 (Lightweight 40x40)
- **Data Preparation:** `python Autopilot/LoadData.py` (Outputs isolated `features_40.pkl` and `labels_40.pkl`)
- **Training:** `python Autopilot/TrainModel.py` (Trains and outputs `models/Autopilot_V1.h5`)
- **Inference UI:** `python Autopilot/DriveApp.py Autopilot/resources/harder_challenge_video.mp4`

### Running Version 2 (Advanced 100x100)
- **Data Preparation:** `python Autopilot_V2/LoadData_V2.py` (Outputs `features` and `labels` pkl files from the CSV log)
- **Training:** `python Autopilot_V2/Train_pilot_V2.py` (Trains and outputs `models/Autopilot_V2.h5`)
- **Inference UI:** `python Autopilot_V2/AutopilotApp_V2.py Autopilot/resources/harder_challenge_video.mp4`

## 5. Inference Results

**Day Time Conditions:**
![Day Time Conditions](day_time_conditions.png)

**Dark Light Conditions:**
![Dark Light Conditions](dark_light_conditions.png)

## 6. Current State & Retraining
- **Environment Constraints:** Legacy `.h5` models contained pickled lambda operations ("marshal data") that became incompatible in newer Python 3.10 and Keras 3 versions.
- **Resolution:** A fresh Python venv was created with `tensorflow==2.15.0` and `keras==2.15.0`. We natively downloaded the 317MB Udacity driving dataset and completely retrained the V2 Convolutional Neural Network from scratch.
- **Resources:** The inference application seamlessly handles new road tracks like `challenge_video.mp4` smoothly applying the CNN's steering predictions to the visual wheel overlay.

