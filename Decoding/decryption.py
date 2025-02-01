import cv2
import numpy as np

# Function to deskew the image by rotating it
def deskew_image(image, angle):
    # Get the image center
    center = (image.shape[1] // 2, image.shape[0] // 2)

    # Create the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

    return rotated_image

# Read the original image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error: Unable to read the image!")
    exit(1)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the deskew (rotate by -4 degrees based on the previous result)
deskewed_image = deskew_image(gray_image, -4)

# Save and display the deskewed grayscale image
cv2.imwrite("deskewed_image.png", deskewed_image)
cv2.imshow("Deskewed Grayscale Image", deskewed_image)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
