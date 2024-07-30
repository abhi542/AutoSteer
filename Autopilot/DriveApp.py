import os
import numpy as np
import cv2
from keras.models import load_model
import keras

# Enable unsafe deserialization
keras.config.enable_unsafe_deserialization()

# Load the trained model
model_path = os.path.join('Autopilot', 'models', 'Autopilot.keras')
model = load_model(model_path)

def keras_predict(model, image):
    processed = keras_process_image(image)
    steering_angle = float(model.predict(processed, batch_size=1))
    steering_angle = steering_angle * 100 
    return steering_angle 

def keras_process_image(img):
    image_x = 40
    image_y = 40
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, image_x, image_y, 1))
    return img

# Load the steering wheel image
steering_wheel_image_path = os.path.join('Autopilot', 'resources', 'steering_wheel_image.jpg')
steer = cv2.imread(steering_wheel_image_path, 0)
if steer is None:
    print(f"Error: Steering wheel image not found. Check the file path: {steering_wheel_image_path}")
    exit()

rows, cols = steer.shape
smoothed_angle = 0

# Load the video
video_path = os.path.join('Autopilot', 'resources', 'run.mp4')
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Video file not found. Check the file path: {video_path}")
    exit()

# Create named windows and set them to resizable
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.namedWindow('steering wheel', cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.resize((cv2.cvtColor(frame, cv2.COLOR_RGB2HSV))[:, :, 1], (40, 40))
    steering_angle = keras_predict(model, gray)
    print(f"Steering angle: {steering_angle}")

    # Display the frame and the steering angle on the frame
    frame_resized = cv2.resize(frame, (500, 300), interpolation=cv2.INTER_AREA)
    cv2.putText(frame_resized, f"Steering Angle: {steering_angle:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    smoothed_angle += 0.2 * pow(abs((steering_angle - smoothed_angle)), 2.0 / 3.0) * (
        steering_angle - smoothed_angle) / abs(
        steering_angle - smoothed_angle)
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -smoothed_angle, 1)
    dst = cv2.warpAffine(steer, M, (cols, rows))
    
    cv2.imshow('frame', frame_resized)
    cv2.imshow('steering wheel', dst)
    
    # Slow down the video by adding a delay
    cv2.waitKey(50)  # Adjust the delay time (in milliseconds) to slow down processing

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



















################### v4 




