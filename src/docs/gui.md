## PyCGUI Class

The `PyCGUI` class represents a graphical user interface for controlling camera functions and displaying live video feed with filters.

**Author:** Iágson Carlos Lima Silva  
**Copyright:** Copyright (c) 2023 @iagsoncarlos  
**Created:** Tuesday, August 15, 2023

### Constructor

```python
class PyCGUI(QMainWindow):
    def __init__(self):
        """
        Initialize the PyCGUI object.

        This constructor sets up the main window, UI elements, camera instance, and event handlers.
        """
```

### Methods

#### `setup_url_input`

```python
    def setup_url_input(self):
        """
        Set up the input field and button for changing the camera's URL.

        This method creates UI elements to input a new camera URL and updates the camera source accordingly.
        """
```

#### `setup_control_buttons`

```python
    def setup_control_buttons(self):
        """Set up the control buttons for recording and capturing photos."""
```

#### `setup_filter_buttons`

```python
    def setup_filter_buttons(self):
        """Set up buttons for selecting camera filters."""
```

#### `setup_filter_dropdown`

```python
    def setup_filter_dropdown(self):
        """Set up a dropdown list for selecting camera filters."""
```

#### `set_filter`

```python
    def set_filter(self, filter_name):
        """Set the current camera filter."""
```

#### `change_camera_url`

```python
    def change_camera_url(self):
        """Change the camera's URL based on user input."""
```

#### `display`

```python
    def display(self):
        """
        Update the displayed camera feed with the selected filter and handle recording indicators.

        This method captures frames from the camera, applies the chosen filter, and displays the video feed.
        Additionally, it supports recording functionality by overlaying a "REC" indicator on the frame.
        """
```

#### `toggle_recording`

```python
    def toggle_recording(self):
        """Toggle camera recording and update button text."""
```

#### `capture_photo`

```python
    def capture_photo(self):
        """Capture a photo using the camera."""
```

#### `apply_filter`

```python
    def apply_filter(self, filter_name):
        """Apply the specified filter to the camera feed."""
```

#### `closeEvent`

```python
    def closeEvent(self, event):
        """
        Handle the closing of the application and clean up camera resources.

        This method is triggered when the user attempts to close the application.
        It stops any ongoing recording, releases the camera resources, and allows the application to close gracefully.
        """
```

### Usage Examples

#### Create and Display GUI

```python
app = QApplication(sys.argv)
gui = PyCGUI()
gui.show()
sys.exit(app.exec_())
```

---

Feel free to replace the class's initial comment block with this Markdown documentation, including the added usage examples. This should provide comprehensive information on how to use the `PyCGUI` class and its methods.