import cv2
import numpy as np
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Give the camera some time to warm up
print("Getting background. Please move out of the frame...")
time.sleep(2)

# Capture the background
for i in range(30):
    ret, background = cap.read()
    if not ret:
        print("Failed to capture background. Please check your camera.")
        cap.release()
        cv2.destroyAllWindows()
        exit()

# Flip the background
background = np.flip(background, axis=1)

print("Background captured. You may now step into the frame wearing a black cloth.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural (mirror) view
    frame = np.flip(frame, axis=1)

    # Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the HSV range for black color
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    # Create a binary mask for detecting black
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Refine the mask using morphological operations
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

    # Create the inverse mask
    mask_inverse = cv2.bitwise_not(mask)

    # Segment out the black color part from the background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Segment the rest of the frame (non-cloak area)
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inverse)

    # Combine both to get the final output
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    # Show the output
    cv2.imshow("Invisibility Cloak - Black Cloak Edition", final_output)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
