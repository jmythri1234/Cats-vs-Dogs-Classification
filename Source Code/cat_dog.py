import cv2
import numpy as np

# Load images
cat = cv2.imread(r"C:\Users\jikka\OneDrive\Pictures\cute_cat.jpg")
dog = cv2.imread(r"C:\Users\jikka\OneDrive\Pictures\cute_dog.jpg")

# Resize images
cat = cv2.resize(cat, (400, 350))
dog = cv2.resize(dog, (400, 350))

# Create white background
output = np.ones((700, 1000, 3), dtype="uint8") * 255

# Headings
cv2.putText(
    output,
    "Prediction: Cat",
    (120, 60),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 0),
    2
)

cv2.putText(
    output,
    "Prediction: Dog",
    (620, 60),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 0),
    2
)

# Place images
output[120:470, 50:450] = cat
output[120:470, 550:950] = dog

# Fullscreen window
cv2.namedWindow("Cat and Dog Classifier", cv2.WND_PROP_FULLSCREEN)

cv2.setWindowProperty(
    "Cat and Dog Classifier",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

# Show output
cv2.imshow("Cat and Dog Classifier", output)

cv2.waitKey(0)
cv2.destroyAllWindows()