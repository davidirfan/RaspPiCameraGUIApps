# this program is to open a window to get the preview of Raspberry Pi camera

import tkinter as tk
from picamera2 import Picamera2
from PIL import Image, ImageTk

# Create a function to update the camera feed in the Tkinter window
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

# Start updating the camera feed
update_frame()

# Start the Tkinter main loop
window.mainloop()

# Stop the camera when the window is closed
picam2.stop()
