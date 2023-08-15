#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Iágson Carlos Lima Silva on Tuesday, August 15, 2023.
# Copyright (c) 2023 @iagsoncarlos. All rights reserved.

__author__      = 'Iágson Carlos Lima Silva'
__copyright__   = 'Copyright (c) 2023 @iagsoncarlos'

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QSizePolicy, QHBoxLayout, QLineEdit, QComboBox

from core.pyc import Camera


class PyCGUI(QMainWindow):
    """
    A graphical user interface for controlling camera functions and displaying live video feed with filters.

    This class initializes a PyQt-based GUI application that interacts with a camera to display real-time video
    feed and provides options for selecting filters, capturing photos, and recording videos.
    """
    def __init__(self):
        super().__init__()

        # Initialize instance variables
        self.camera = None
        self.recording = False
        self.current_filter_name = 'None'

        # Set up main window properties
        self.setWindowTitle("PyC")
        self.setGeometry(100, 100, 1000, 680) # Set initial position and size (x, y, w, h)
        self.setMinimumSize(400, 300)

        # Create central widget for layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the main vertical layout
        self.central_layout = QVBoxLayout(self.central_widget)

        # Create a label for displaying the camera feed
        self.image_label = QLabel(self)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.central_layout.addWidget(self.image_label, 1)

        # Set up URL input and control buttons
        self.setup_url_input()
        self.setup_control_buttons()

        # Create the camera instance
        self.camera = Camera()

        # Set up filter selection buttons
        self.setup_filter_buttons()     # Filters like buttons
        # self.setup_filter_dropdown()     # Filters like dropdown


        # Create a timer for updating the camera feed display
        self.camera_timer = QTimer(self)
        self.camera_timer.timeout.connect(self.display)
        self.camera_timer.start(30)

        self.recording = False

    def setup_url_input(self):
        """
        Set up the input field and button for changing the camera's URL.

        This method creates UI elements to input a new camera URL and updates the camera source accordingly.
        """
        url_layout = QHBoxLayout()
        self.url_input = QLineEdit(self)
        url_layout.addWidget(self.url_input)

        self.change_url_button = QPushButton("Change URL", self)
        self.change_url_button.clicked.connect(self.change_camera_url)
        url_layout.addWidget(self.change_url_button)

        self.central_layout.addLayout(url_layout)

    def setup_control_buttons(self):
        """Set up the control buttons for recording and capturing photos."""
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Recording", self)
        self.start_button.clicked.connect(self.toggle_recording)
        button_layout.addWidget(self.start_button)

        self.capture_button = QPushButton("Capture Photo", self)
        self.capture_button.clicked.connect(self.capture_photo)
        button_layout.addWidget(self.capture_button)

        self.central_layout.addLayout(button_layout)

    def setup_filter_buttons(self):
        """Set up buttons for selecting camera filters."""
        filter_layout = QHBoxLayout()

        for filter_name in self.camera.filters:
            filter_button = QPushButton(filter_name, self)
            filter_button.clicked.connect(lambda _, name=filter_name: self.set_filter(name))
            filter_layout.addWidget(filter_button)

        self.central_layout.addLayout(filter_layout)

    def setup_filter_dropdown(self):
        """Set up a dropdown list for selecting camera filters."""
        self.filter_dropdown = QComboBox(self)
        for filter_name in self.camera.filters:
            self.filter_dropdown.addItem(filter_name)
        self.filter_dropdown.activated[str].connect(self.set_filter)
        self.central_layout.addWidget(self.filter_dropdown)

    def set_filter(self, filter_name):
        """Set the current camera filter."""
        self.current_filter_name = filter_name

    def change_camera_url(self):
        """Change the camera's URL based on user input."""
        new_url = self.url_input.text()

        if new_url.isdigit():
            new_url = int(new_url)
        else:
            new_url = new_url.strip()

        if self.camera is not None:
            self.camera.capture.release()
        self.camera = Camera(new_url)
        self.recording = False

    def display(self):
        """
        Update the displayed camera feed with the selected filter and handle recording indicators.

        This method captures frames from the camera, applies the chosen filter, and displays the video feed.
        Additionally, it supports recording functionality by overlaying a "REC" indicator on the frame.
        """
        if self.camera is None:
            return

        ret, frame = self.camera.capture.read()
        if ret:
            filtered_frame = self.camera.apply_filter(frame, self.current_filter_name)

            self.frame = filtered_frame

            # Convert color format and resize the frame for display
            rgb_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape

            label_width = self.image_label.width()
            label_height = self.image_label.height()

            image_aspect_ratio = w / h
            label_aspect_ratio = label_width / label_height

            if image_aspect_ratio > label_aspect_ratio:
                new_width = label_width
                new_height = int(label_width / image_aspect_ratio)
            else:
                new_width = int(label_height * image_aspect_ratio)
                new_height = label_height

            resized_frame = cv2.resize(rgb_frame, (new_width, new_height))

            bytes_per_line = ch * new_width

            # Add recording indicator and display the frame
            if self.recording:
                cv2.circle(resized_frame, (30, 19), 7, (255, 0, 0), -1)
                cv2.putText(resized_frame, "REC", (50, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0))
                self.camera.out.write(filtered_frame)

            q_image = QImage(resized_frame.data, new_width, new_height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

    def toggle_recording(self):
        """Toggle camera recording and update button text."""
        if self.camera is None:
            return

        if not self.recording:
            self.camera.start_recording()
            self.start_button.setText("Stop Recording")
        else:
            self.camera.stop_recording()
            self.start_button.setText("Start Recording")
        self.recording = not self.recording

    def capture_photo(self):
        """Capture a photo using the camera."""
        if self.camera is not None:
            self.camera.capture_photo(self.frame)

    def apply_filter(self, filter_name):
        """Apply the specified filter to the camera feed."""
        self.current_filter_name = filter_name

    def closeEvent(self, event):
        """
        Handle the closing of the application and clean up camera resources.

        This method is triggered when the user attempts to close the application.
        It stops any ongoing recording, releases the camera resources, and allows the application to close gracefully.
        """
        if self.camera is not None and self.camera.recording:
            self.camera.stop_recording()
        if self.camera is not None:
            self.camera.capture.release()
        event.accept()
