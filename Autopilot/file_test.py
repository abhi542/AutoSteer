import os
import cv2

# Print current working directory to verify
print(f"Current working directory: {os.getcwd()}")

# Define the path to the steering wheel image
steer_path = os.path.join('Autopilot', 'resources', 'steering_wheel_image.jpg')
print(f"Looking for steering wheel image at: {steer_path}")

# Check if the file exists
if not os.path.exists(steer_path):
    raise FileNotFoundError(f"Steering wheel image not found: {steer_path}")

# Attempt to read the image
steer = cv2.imread(steer_path, 0)
if steer is None:
    raise FileNotFoundError(f"Error loading steering wheel image: {steer_path}")

print("Steering wheel image loaded successfully.")
