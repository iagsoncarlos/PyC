## Camera Class

The `Camera` class manages camera operations, including capturing photos and recording videos.

**Author:** Iágson Carlos Lima Silva  
**Copyright:** Copyright (c) 2023 @iagsoncarlos  
**Created:** Tuesday, August 15, 2023

### Constructor

```python
class Camera:
    def __init__(self, index: int | str = 0):
        """
        Initialize the Camera object with an optional camera index.

        Args:
            index (int | str): Camera index (default is 0 for the default camera).
        """
```

### Methods

#### `update_fps`

```python
    def update_fps(self, duration=3):
        """
        Calculate the average frames per second (FPS) over a specified duration.

        Args:
            duration: Duration in seconds to calculate average FPS over (default is 3 seconds).
        """
```

#### `apply_filter`

```python
    def apply_filter(self, frame, filter_name):
        """
        Apply the selected filter to the input frame.

        Args:
            frame: Input frame.
            filter_name: Name of the filter to be applied.

        Returns:
            Filtered frame.
        """
```

#### `face_detection`

```python
    def face_detection(self, frame):
        """
        Perform face detection on the input frame.

        Args:
            frame: Input frame.

        Returns:
            Frame with face detection rectangles drawn.
        """
```

#### `start_recording`

```python
    def start_recording(self, output_path=None):
        """
        Start recording video from the camera.

        Args:
            output_path (str): Path to save the recorded video. If not provided, a default filename will be used.
        """
```

#### `stop_recording`

```python
    def stop_recording(self):
        """
        Stop the ongoing video recording.
        """
```

#### `capture_photo`

```python
    def capture_photo(self, frame, output_path=None):
        """
        Capture a photo from the camera and save it as an image file.

        Args:
            frame (numpy.ndarray): The frame to capture as a photo.
            output_path (str): Path to save the captured photo. If not provided, a default filename will be used.
        """
```

#### `display`

```python
    def display(self, zoom=100):
        """
        Display the camera feed and handle user interactions.

        Args:
            zoom: Zoom level for display.
        """
```

### Usage Examples

#### Initialize a Camera Object

```python
camera = Camera()  # Initializes the camera with default index 0
```

#### Update FPS

```python
camera.update_fps()  # Calculates and prints average FPS over the default 3 seconds
```

#### Apply Filters

```python
filtered_frame = camera.apply_filter(frame, 'Grayscale')  # Applies the grayscale filter to the input frame
```

#### Start and Stop Recording

```python
camera.start_recording()  # Starts recording video
camera.stop_recording()   # Stops the ongoing video recording
```

#### Capture Photo

```python
camera.capture_photo(frame)  # Captures and saves a photo from the input frame
```

#### Display Camera Feed

```python
camera.display(zoom=80)  # Displays the camera feed with a zoom level of 80%
```

---

Feel free to replace the class's initial comment block with this Markdown documentation, including the added usage examples. This should provide comprehensive information on how to use the `Camera` class and its methods.