import tkinter as tk
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from PIL import Image, ImageTk
import os
import datetime

# Create directories for saving photos and videos
PHOTO_DIR = "photos"
VIDEO_DIR = "videos"
os.makedirs(PHOTO_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

# Initialize Picamera2
picam2 = Picamera2()

# Configure the camera for both video and photo capture
camera_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)

# Function to toggle auto-focus settings (note: depends on camera support)
def toggle_auto_focus():
    # Enable or disable auto exposure and auto white balance for clarity
    picam2.set_controls({"AfMode": 2, "AeEnable": True, "AwbEnable": True})
    print("Auto-focus enabled")
    
# Function to improve clarity by adjusting settings
def set_clarity_settings():
    # You can manually adjust the camera settings for better clarity
    picam2.set_controls({
        "ExposureTime": 10000,  # Example exposure time
        "AnalogueGain": 1.0,  # ISO
        "Sharpness": 1.0,  # Increase sharpness
        "Contrast": 1.0  # Adjust contrast
    })
    print("Clarity settings applied")

# Function to start video recording
def start_recording():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    video_file_path = os.path.join(VIDEO_DIR, f"video_{timestamp}.h264")
    
    picam2.start_recording(H264Encoder(), video_file_path)
    print(f"Recording started: {video_file_path}")

# Function to stop video recording
def stop_recording():
    picam2.stop_recording()
    print("Recording stopped.")

# Function to take a photo
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
    file_path = os.path.join(PHOTO_DIR, f"photo_{timestamp}.jpg")

    # Save the image
    frame_image.save(file_path)
    print(f"Photo saved: {file_path}")
    
# Function to update the preview in the Tkinter window
def update_preview():
    frame = picam2.capture_array()
    img = Image.fromarray(frame)
    img = img.resize((680, 480))  # Resize for preview window
    img_tk = ImageTk.PhotoImage(image=img)

    label_preview.config(image=img_tk)
    label_preview.image = img_tk
    window.after(100, update_preview)  # Update every 100ms

# Initialize the Tkinter window
window = tk.Tk()
window.title("Photo and Video Recorder")

# Create preview label
label_preview = tk.Label(window)
label_preview.pack(pady=10)

# Create a "Take Photo" button
photo_button = tk.Button(window, text="Take Photo", command=take_photo)
photo_button.pack(pady=10)

# Create "Start Recording" and "Stop Recording" buttons
start_button = tk.Button(window, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

# Create "Toggle Auto Focus" button
focus_button = tk.Button(window, text="Toggle Auto Focus", command=toggle_auto_focus)
focus_button.pack(pady=10)

# Create "Set Clarity Settings" button
clarity_button = tk.Button(window, text="Set Clarity", command=set_clarity_settings)
clarity_button.pack(pady=10)

# Start the camera and preview
picam2.start()
update_preview()

# Run the Tkinter main loop
window.mainloop()

# Stop the camera when the window is closed
picam2.stop()
