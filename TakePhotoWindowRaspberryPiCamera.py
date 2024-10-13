# this program to open the window to open preview camera and take photo using "Take Photo" button that provide in that window

import tkinter as tk
from picamera2 import Picamera2
from PIL import Image, ImageTk
import os
import datetime

# Define the directory where photos will be saved
SAVE_DIR = "photos"
os.makedirs(SAVE_DIR, exist_ok=True)  # Create the directory if it doesn't exist

# Function to capture and save the current frame
def take_photo():
    # Capture the current frame from the camera
    frame = picam2.capture_array()

    # Convert the frame to an image
    frame_image = Image.fromarray(frame)
    
    # Convert to RGB if the image is in RGBA mode
    if frame_image.mode == 'RGBA':
        frame_image = frame_image.convert('RGB')

    # Create a unique filename based on the current time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(SAVE_DIR, f"photo_{timestamp}.jpg")

    # Save the image
    frame_image.save(file_path)

    print(f"Photo saved: {file_path}")

# Function to update the camera feed in the Tkinter window
def update_frame():
    frame = picam2.capture_array()
    frame_image = Image.fromarray(frame)
    frame_photo = ImageTk.PhotoImage(frame_image)

    # Update the label with the new frame
    label.config(image=frame_photo)
    label.image = frame_photo

    # Call this function again after a short delay
    window.after(10, update_frame)  # 10ms delay for smooth updates

# Initialize Tkinter window
window = tk.Tk()
window.title("Camera Preview")

# Initialize Picamera2
picam2 = Picamera2()

# Configure the camera
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

# Start the camera
picam2.start()

# Create a label to hold the camera feed
label = tk.Label(window)
label.pack()

# Create a "Take Photo" button
take_photo_button = tk.Button(window, text="Take Photo", command=take_photo)
take_photo_button.pack(pady=10)

# Start updating the camera feed
update_frame()

# Start the Tkinter main loop
window.mainloop()

# Stop the camera when the window is closed
picam2.stop()
