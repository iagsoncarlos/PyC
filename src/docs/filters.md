# PyC - Camera Filters Documentation

PyC provides a versatile set of filters that you can apply to the camera feed, offering a wide range of creative effects to enhance your media content. Each filter modifies the appearance of the video stream in real-time, providing you with opportunities to experiment and tailor your visual content. Below is an in-depth look at the available filters, along with explanations of their uses and code examples using the OpenCV library.

## Available Filters

### None

**Description**: No filter is applied to the camera feed, providing the unaltered video stream.

**Use Cases**: The "None" filter is ideal for capturing authentic and unmodified video content. It is suitable for scenarios where you want to maintain the original visual representation without any alterations.

### Grayscale

**Description**: Converts the camera feed to grayscale, creating a classic black-and-white appearance.

**Use Cases**: Grayscale is a timeless choice for adding a vintage or nostalgic vibe to your media. It simplifies the visual elements and can draw attention to specific details in the frame, making it great for emphasizing shapes, textures, and contrasts.

**Code Example**:
```python
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

### Edge Detection

**Description**: Applies edge detection to the camera feed, highlighting prominent edges and boundaries.

**Use Cases**: Edge detection is valuable for emphasizing object outlines and shapes. It's commonly used in scenarios where identifying edges or boundaries is crucial, such as object recognition or enhancing architectural details.

**Code Example**:
```python
edges = cv2.Canny(frame, threshold1=30, threshold2=70)
```

### Color Inversion

**Description**: Inverts the colors of the camera feed, resulting in a color-negative effect.

**Use Cases**: Color inversion can create surreal or dramatic effects in your media. It's often used to convey alternate realities, dream sequences, or to evoke emotional responses.

**Code Example**:
```python
inverted_frame = cv2.bitwise_not(frame)
```

### Binarization

**Description**: Converts the camera feed to a binary image, emphasizing high-contrast areas.

**Use Cases**: Binarization simplifies the image by dividing it into just two colors, making it effective for scenarios where you need to focus on the presence or absence of specific features, such as text extraction or image segmentation.

**Code Example**:
```python
_, binary_frame = cv2.threshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 128, 255, cv2.THRESH_BINARY)
```

### Mean Filter

**Description**: Applies a mean filter to the camera feed, creating a smoothing effect.

**Use Cases**: The mean filter reduces noise and small details in the image, resulting in a soft and cohesive appearance. It's useful for blurring imperfections or reducing image noise.

**Code Example**:
```python
smoothed_frame = cv2.blur(frame, (7, 7))
```

### Median Filter

**Description**: Applies a median filter to the camera feed, effectively reducing noise.

**Use Cases**: The median filter is particularly effective in removing salt-and-pepper noise, which are random black and white pixels. It's ideal for enhancing images captured in low-light conditions or through noisy channels.

**Code Example**:
```python
denoised_frame = cv2.medianBlur(frame, 7)
```

### Gaussian Blur

**Description**: Applies a Gaussian blur to the camera feed, creating a softening effect.

**Use Cases**: Gaussian blur provides a gentle smoothing effect, making it suitable for concealing small details and imperfections. It's often used for portrait photography to achieve a soft, dreamy appearance.

**Code Example**:
```python
blurred_frame = cv2.GaussianBlur(frame, (7, 7), 0)
```

### Face Detection

**Description**: Performs face detection on the camera feed and highlights detected faces with rectangles.

**Use Cases**: Face detection is essential for identifying and tracking human faces in images or videos. It's commonly used in applications like video conferencing, security systems, and automatic tagging.

**Code Example**:
```python
face_cascade = cv2.CascadeClassifier("path_to_haarcascade.xml")
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
```

## Applying Filters

To apply any of these filters to the camera feed in the PyC application, follow these steps:

1. Launch the PyC application.
2. Navigate to the "Filters" section.
3. Click on the button corresponding to the desired filter.

The camera feed displayed in the application will instantly reflect the chosen filter, allowing you to preview the effect in real-time. Experiment with different filters to achieve the desired visual effect for your media content.

## Additional Information

Each filter offers a distinct effect on the camera feed, allowing you to enhance your media content creatively. Understanding these filters' purposes and use cases will help you make informed decisions to create captivating visuals.

---

This detailed documentation provides comprehensive information about each filter's description, use cases, and code examples using the OpenCV library. It will assist you in utilizing filters effectively to enhance your media content in the PyC application.

## References

Gonzalez,  R.C.  and  Woods,  R.E.,  Digital  Image  Processing,  3rd  Edition,  Pearson-Prentice-Hall, 2008.

OpenCV - Open Source Computer Vision Library. Available from: https://docs.opencv.org/4.x/. Accessed on: (08/17/2023).
