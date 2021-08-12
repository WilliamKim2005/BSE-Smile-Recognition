import cv2 # OpenCV
import numpy as np # Numpy

print("Running OpenCV Camera test")
cap = cv2.VideoCapture(0) # Enables video capturing object on Camera
while True:
    _, frame = cap.read() # Read each frame from Camera
    cv2.imshow("Frame", frame) # Show frame captured from video

    # Press Q to End
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Q pressed")
        break

print("Successful")
cap.release() # Releases object from Camera
cv2.destroyAllWindows() # Destroys all windows