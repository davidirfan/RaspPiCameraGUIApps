# this program is to open a window to preview camera and records video using Raspberry Pi Camera

import tkinter as tk
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from PIL import Image, ImageTk
import os
import datetime

# Define the directory where videos will be saved
VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)  # Create the directory if it doesn't exist

# Initialize Picamera2
picam2 = Picamera2()

# Configure the camera for video recording
camera_config = picam2.create_video_configuration()
picam2.configure(camera_config)

# Function to update the preview in the Tkinter window
def update_preview():
    frame = picam2.capture_array()
    img = Image.fromarray(frame)
    img = img.resize((680, 480))  # Resize for preview window
    img_tk = ImageTk.PhotoImage(image=img)

    label_preview.config(image=img_tk)
    label_preview.image = img_tk
    window.after(100, update_preview)  # Update every 100ms

# Function to start video recording
def start_recording():
    # Generate a unique filename based on the current time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    video_file_path = os.path.join(VIDEO_DIR, f"video_{timestamp}.h264")

    # Start recording the video
    picam2.start_recording(H264Encoder(), video_file_path)
    print(f"Recording started: {video_file_path}")

# Function to stop video recording
def stop_recording():
    # Stop recording the video
    picam2.stop_recording()
    print("Recording stopped.")

# Initialize Tkinter window
window = tk.Tk()
window.title("Video Recorder")

# Create preview label
label_preview = tk.Label(window)
label_preview.pack(pady=10)

# Create a "Start Recording" button
start_button = tk.Button(window, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

# Create a "Stop Recording" button
stop_button = tk.Button(window, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

# Start the camera and preview
picam2.start()
update_preview()

# Start the Tkinter main loop
window.mainloop()

# Stop the camera when the window is closed
picam2.stop()
