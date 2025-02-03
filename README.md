# Object-Tracking
Overview

This project demonstrates real-time object tracking using the OpenCV library. The application allows users to track an object in a video stream (e.g., from a webcam). It utilizes the CSRT tracker for tracking an object selected by the user in the first frame. The object is tracked as it moves in the video.

The project provides a simple and efficient way to track an object in real time, using the OpenCV DNN module and Python.

Features

Real-time object tracking using the CSRT tracker (accurate and robust).
Select the object to track using a simple bounding box in the first frame.
The program continues to track the selected object throughout the video stream.
The object’s position is updated, and a bounding box is drawn around it.
Requirements

Python 3.x
OpenCV 4.x (with opencv-contrib-python package for CSRT tracker)
Numpy
Installation

Step 1: Clone the Repository
Clone the repository to your local machine.

git clone https://github.com/your-username/object-tracking.git
cd object-tracking
Step 2: Set up the Python Environment
It’s recommended to use a virtual environment for this project to manage dependencies.

python3 -m venv object_tracking_env
source object_tracking_env/bin/activate  # On macOS/Linux
# For Windows use: object_tracking_env\Scripts\activate
Step 3: Install Dependencies
Install the required libraries using pip.

pip install opencv-contrib-python numpy
This will install:

OpenCV (including the contrib modules)
Numpy (used for array manipulation)
Step 4: Test OpenCV Installation
Make sure OpenCV is installed correctly by running this Python snippet:

import cv2
print(cv2.__version__)
If the version is printed without errors, the installation was successful.

Usage

Step 1: Run the Script
Execute the Python script to start the object tracking.

python object_tracking.py
The program will open a window displaying the video stream from your webcam.

Step 2: Select Object to Track
Select a Region of Interest (ROI): In the video stream window, use your mouse to draw a bounding box around the object you want to track.
Press ENTER or SPACE to confirm the selection.
Press ESC to exit the program.
Step 3: Track the Object
The selected object will be tracked, and a green bounding box will be drawn around it as it moves in the video stream.

Key Presses:
ENTER or SPACE: Confirm the selected object for tracking.
ESC: Exit the program.
c: Cancel the current ROI selection.
Code Structure

The project consists of the following files:

object_tracking.py: The main script to run the object tracking program.
README.md: This file.
object_tracking.py Explanation:
Capture Video Stream: Using OpenCV’s cv2.VideoCapture(0) to capture video from the webcam.
Select ROI: The cv2.selectROI() function allows the user to select an object for tracking.
CSRT Tracker: The cv2.TrackerCSRT_create() initializes the CSRT tracker, which is used to track the selected object across the video frames.
Tracking Loop: The program continually updates the object’s position in the video stream and draws the bounding box around it.
Exit: The program will exit when the ESC key is pressed.
Troubleshooting

1. Tracker Not Found:
If you get an error related to the tracker not being found (e.g., AttributeError: module 'cv2' has no attribute 'TrackerCSRT_create'), ensure that you have installed the opencv-contrib-python package, which contains the necessary tracking algorithms:

pip install opencv-contrib-python
2. Webcam Not Detected:
If your webcam isn't detected, ensure that it is correctly connected to your system and recognized by the operating system. Try using a different USB port or restarting your computer.

3. Performance Issues:
If the tracking is lagging or not responsive, consider switching to a different tracker, like the KCF tracker:

tracker = cv2.TrackerKCF_create()
However, CSRT is typically the most accurate but slower. Adjusting the resolution or using a more powerful machine can improve performance.

Contributions

Feel free to fork this project and submit pull requests for improvements, bug fixes, or new features. Contributions are always welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.
