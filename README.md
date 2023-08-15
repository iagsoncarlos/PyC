# PyC - Camera Application

A graphical user interface for controlling camera functions and displaying live video feed with filters.

## Installation and Requirements

- Make sure you have Python 3.x installed.
- Install required dependencies using the following command:
  ```sh
  pip install opencv-python PyQt5
  ```

## Usage

1. Run the application:
   ```sh
   python src/main.py
   ```
2. Change the camera source URL using the input field and "Change URL" button.
3. Use the control buttons to start/stop recording and capture photos.
4. Click on filter buttons to apply different filters to the camera feed.

## Screenshots

![!\[Alt text\](<!\[assets/screenshot.png\](src/assets/screenshot.png)>)](src/assets/screenshot.png)

## Project Explanation

- `main.py`: This file contains the main application logic and user interface setup.
- `core/pyc.py`: This module manages camera operations and filter application.
- `interface/gui.py`: This module manages camera interface with operations and filter application.
- `models/haarcascade_frontalface_default.xml`:  The `haarcascade_frontalface_default.xml` file is a cascade XML file used for face detection. It is part of the OpenCV library and is widely used in face detection tasks. The file contains information about facial features and appearance patterns that are used by the face detection algorithm.

For more information about the file and its usage, see the [official OpenCV documentation](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

## License and Copyright

- This project is licensed under the MIT License.
- Copyright (c) 2023 Iágson Carlos Lima Silva

## Contact Information

For questions or feedback, you can reach out to me at @iagsoncarlos