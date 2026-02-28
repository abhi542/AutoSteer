import cv2
import os
import sys
import numpy as np
import pickle
import csv
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

    target_dir = sys.argv[1] if len(sys.argv) > 1 else DATA_FOLDER
    csv_path = os.path.join(target_dir, 'driving_log.csv')
    
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found")
        return
        
    logs = []
    with open(csv_path, 'rt') as f:
        reader = csv.reader(f)
        for line in reader:
            logs.append(line)
        log_labels = logs.pop(0)  # Remove headers
        
    for i in range(min(LIMIT, len(logs))):
        # Center image
        img_path = logs[i][0]
        full_path = target_dir + '/IMG' + (img_path.split('IMG')[1]).strip()
        X.append(full_path)
        y.append(float(logs[i][3]))

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
