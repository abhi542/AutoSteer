from __future__ import division
import cv2
import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
from itertools import islice

LIMIT = 10000

DATA_FOLDER = 'driving_dataset'
TRAIN_FILE = os.path.join(DATA_FOLDER, 'data.txt')

def preprocess(img):
    resized = cv2.resize(cv2.cvtColor(img, cv2.COLOR_RGB2HSV)[:, :, 1], (100, 100))
    return resized

def return_data():

    X = []
    y = []
    features = []

    with open(TRAIN_FILE) as fp:
        for line in islice(fp, LIMIT):
            path, angle = line.strip().split()
            full_path = os.path.join(DATA_FOLDER, path)
            X.append(full_path)
            y.append(float(angle) * np.pi / 180)  # Changed scipy.pi to np.pi

    for i in range(len(X)):
        img = cv2.imread(X[i])  # Using cv2.imread instead of plt.imread
        if img is None:
            print(f"Error loading image: {X[i]}")
            continue
        features.append(preprocess(img))

    features = np.array(features).astype('float32')
    labels = np.array(y).astype('float32')

    with open("features", "wb") as f:
        pickle.dump(features, f, protocol=4)
    with open("labels", "wb") as f:
        pickle.dump(labels, f, protocol=4)

return_data()
