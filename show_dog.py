import cv2
import numpy as np

# Load dog image
img = cv2.imread(r"C:\Users\jikka\OneDrive\Pictures\cute_dog.jpg")

# Resize image
img = cv2.resize(img, (700, 500))

# Create white background
output = np.ones((700, 1000, 3), dtype="uint8") * 255

# Heading
cv2.putText(
    output,
    "Prediction: Dog",
    (330, 60),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    (0, 0, 0),
    3
)

# Put image in center
output[120:620, 150:850] = img

# Full screen window
cv2.namedWindow("Dog Classifier", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(
    "Dog Classifier",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

# Show output
cv2.imshow("Dog Classifier", output)

cv2.waitKey(0)
cv2.destroyAllWindows()