## Image Processing Workflow

### Image Preprocessing
- Converts the input image to grayscale.
- Applies Gaussian blur to reduce noise.

### Thresholding
- Uses binary thresholding to separate black and white dots.
- Applies a mask to exclude a noisy region for white dots.

### Contour Detection
- Finds contours for black and white dots.
- Filters contours based on area and intensity.

### Visualization
- Displays the blurred image, binary threshold images, and the final result with detected dots highlighted.

### Return Values
- Returns the number of black and white dots detected.


## Usage

To count the black and white dots, simply update the image path in `final_script.py` with the path to your input image.


## Shortcomings

Currently, an additional mask is used to handle the left side portion of the image while counting white dots. This approach may fail to work with other images. 

To overcome this limitation, a better threshold value can be determined with the help of more sample images.

