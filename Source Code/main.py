import os
import cv2
import numpy as np
import warnings

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
warnings.filterwarnings("ignore")

print("Starting...")

# ---------------- Load Dataset ----------------
data = []
labels = []

dataset_path = "PetImages"
categories = ["Cat", "Dog"]

limit_per_class = 1000

for category in categories:
    folder = os.path.join(dataset_path, category)

    label = categories.index(category)

    count = 0

    for image in os.listdir(folder):

        if count >= limit_per_class:
            break

        try:
            img_path = os.path.join(folder, image)
            img = cv2.imread(img_path)

            if img is None:
                continue

            img = cv2.resize(img, (64, 64))
            img = img.flatten()

            data.append(img)
            labels.append(label)

            count += 1

        except:
            continue

print("\nDataset loaded:", len(data))

# ---------------- Convert ----------------
X = np.array(data)
y = np.array(labels)

# ---------------- Split ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42,stratify=y
)

# ---------------- Train ----------------
print("Training model...")

svm = SVC(kernel='linear', max_iter=10000)

svm.fit(X_train, y_train)

print("Training completed!")

y_pred = svm.predict(X_test)

acc = accuracy_score(y_test, y_pred)

print("Accuracy:", round(acc * 100, 2), "%")
print("Done ✓")