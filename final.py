import cv2
import numpy as np
import matplotlib.pyplot as plt

def count_dots(image_path):
   
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    original = img.copy()

    # Apply Gaussian blur to reduce general noise
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    plt.imshow(blurred, cmap='gray')
    plt.title('Blurred Image')

    # Detect black dots
    _, black_thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY_INV)
    plt.imshow(black_thresh, cmap='gray')
    plt.title('Black Dots Threshold')
    plt.axis('off')

    # Detect white dots
    _, white_thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY)
    
    # Apply mask only to white threshold
    height, width = img.shape
    white_mask = np.ones((height, width), dtype=np.uint8) * 255
    left_margin = int(width * 0.24) # 24% of the width
    white_mask[:, :left_margin] = 0
    white_thresh = cv2.bitwise_and(white_thresh, white_thresh, mask=white_mask)
    plt.imshow(white_thresh, cmap='gray')
    plt.title('White Dots Threshold')
    plt.axis('off')

    # Find contours for black dots
    black_contours, _ = cv2.findContours(
      black_thresh,
      cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE
    )

    # Find contours for black dots
    white_contours, _ = cv2.findContours(
        white_thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    min_area = 5
    max_area = 1000

    black_dots = []
    white_dots = []

    # Filter black dots
    for contour in black_contours:
      area = cv2.contourArea(contour)
      if min_area <= area <= max_area:
          mask = np.zeros_like(img)
          cv2.drawContours(mask, [contour], -1, 255, -1)
          mean_intensity = cv2.mean(img, mask=mask)[0]
          if mean_intensity <= 128:
              black_dots.append(contour)

    # Filter white dots
    for contour in white_contours:
      area = cv2.contourArea(contour)
      if min_area <= area <= max_area:
          mask = np.zeros_like(img)
          cv2.drawContours(mask, [contour], -1, 255, -1)
          mean_intensity = cv2.mean(img, mask=mask)[0]
          if mean_intensity > 100:
              white_dots.append(contour) 
              
    #Results
    result = cv2.cvtColor(original, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(result, black_dots, -1, (0, 0, 255), 2)  # Red for black dots
    cv2.drawContours(result, white_dots, -1, (0, 255, 0), 2)  # Green for white dots

    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title('Detected Dots')                   

    return len(black_dots), len(white_dots)

def process_image(image_path):
    black_count, white_count = count_dots(image_path)
    print(f"Number of black dots: {black_count}")
    print(f"Number of white dots: {white_count}")
    print(f"Total dots: {black_count + white_count}")

image_path = 'pic1.jpg'   
process_image(image_path) 

              



