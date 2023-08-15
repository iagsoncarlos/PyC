#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Iágson Carlos Lima Silva on Tuesday, August 15, 2023.
# Copyright (c) 2023 @iagsoncarlos. All rights reserved.

__author__      = 'Iágson Carlos Lima Silva'
__copyright__   = 'Copyright (c) 2023 @iagsoncarlos'

import os
import cv2
import time
import datetime


class Camera:
    """
    This class manages camera operations, including capturing photos and recording videos.
    """

    def __init__(self, index: int | str = 0):
        """
        Initialize the Camera object with an optional camera index.
        
        Args:
            index (int | str): Camera index (default is 0 for the default camera).
        """
        self.capture = cv2.VideoCapture(index)  # Open the camera using the provided index
        self.recording = False  # Indicates ongoing recording
        self.out = None  # Video writer object
        self.filters = {
            'None': None,
            'Grayscale': lambda img: cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR),
            'Edge Detection': lambda img: cv2.cvtColor(cv2.Canny(img, threshold1=30, threshold2=70), cv2.COLOR_GRAY2BGR),
            'Color Inversion': lambda img: cv2.bitwise_not(img),
            'Binarization': lambda img: cv2.cvtColor(cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 128, 255, cv2.THRESH_BINARY)[1], cv2.COLOR_GRAY2BGR),
            'Mean Filter': lambda img: cv2.blur(img, (7, 7)),
            'Median Filter': lambda img: cv2.medianBlur(img, 7),
            'Gaussian Blur': lambda img: cv2.GaussianBlur(img, (7, 7), 0),
            'Face Detection': lambda img: self.face_detection(img)
            # Add more filters here
        }

    def apply_filter(self, frame, filter_name):
        """
        Apply the selected filter to the input frame.
        
        Args:
            frame: Input frame.
            filter_name: Name of the filter to be applied.
            
        Returns:
            Filtered frame.
        """
        if filter_name in self.filters:
            filter_function = self.filters[filter_name]
            if filter_function:
                return filter_function(frame)
            else:
                return frame
        else:
            return frame

    def face_detection(self, frame):
        """
        Perform face detection on the input frame.

        Docs: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
        
        Args:
            frame: Input frame.
            
        Returns:
            Frame with face detection rectangles drawn.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        face_cascade_path = os.path.join(script_dir, '../models/haarcascade_frontalface_default.xml')  # Replace with actual path
        face_cascade = cv2.CascadeClassifier(face_cascade_path)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame

    def start_recording(self):
        """
        Start recording video from the camera.
        """
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        video_filename = f"video_{current_time}.mp4"

        frame_width = int(self.capture.get(3))
        frame_height = int(self.capture.get(4))

        max_attempts = 2  # Maximum attempts to wait for FPS normalization
        for attempt in range(max_attempts):
            fps = self.capture.get(cv2.CAP_PROP_FPS)
            if fps is None or fps > 1000:  # Check if fetched FPS is too high (likely an error)
                print(f"[INFO] Attempt {attempt + 1}/{max_attempts}: FPS reported too high. Waiting to normalize...")
                time.sleep(2)  # Wait 2 seconds to allow FPS to settle
            else:
                break
        else:
            print("[INFO] Maximum attempts reached or unable to fetch FPS. Proceeding with default FPS.")
            fps = 30  # Set default FPS

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        self.out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))
        self.recording = True

        print("[INFO] Started recording video.")

    def stop_recording(self):
        """
        Stop the ongoing video recording.
        """
        if self.recording:
            self.out.release()  # Release the video writer object
            self.recording = False

            print("[INFO] Stopped recording video.")

    def capture_photo(self, frame):
        """
        Capture a photo from the camera and save it as an image file.
        """
        try:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            photo_filename = f"photo_{current_time}.jpg"

            cv2.imwrite(photo_filename, frame)

            print("[INFO] Photo captured successfully!")
        except:
            print("[INFO] Error capturing photo.")

    def display(self, zoom=100):
        """
        Display the camera feed and handle user interactions.
        
        Args:
            zoom: Zoom level for display.
        """
        current_filter_name = 'None'

        while True:
            ret, frame = self.capture.read()
            if ret:
                filtered_frame = self.apply_filter(frame, current_filter_name)
                if self.recording:
                    bgr_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_GRAY2BGR)
                    self.out.write(bgr_frame)
                display_frame = filtered_frame

                height, width = display_frame.shape[:2]
                new_height = int(height * zoom / 100)
                new_width = int(width * zoom / 100)
                resized_frame = cv2.resize(display_frame, (new_width, new_height))

                cv2.imshow('Camera', resized_frame)

                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
                elif key == ord('p'):
                    self.capture_photo(filtered_frame)
                elif key == ord('r'):
                    if not self.recording:
                        self.start_recording()
                    else:
                        self.stop_recording()
                elif key == ord('0'):
                    current_filter_name = 'None'
                elif ord('1') <= key <= ord('8'):
                    current_filter_name = list(self.filters.keys())[key - ord('0')]

        self.capture.release()
        cv2.destroyAllWindows()
