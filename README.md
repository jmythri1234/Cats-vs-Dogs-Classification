Cats vs Dogs Image Classification Using Support Vector Machine (SVM)

📌 Problem Statement

The objective of this project is to build a Support Vector Machine (SVM) model that can classify images as either Cats or Dogs. The model is trained using image data and learns to distinguish between the two categories based on image features.

📂 Dataset

The project uses the Kaggle Cats and Dogs Dataset, which contains labeled images of cats and dogs for training and testing the classification model.

- Categories: Cat and Dog
- Total Images Used: 2000

🔄 Methodology

- Data Collection and Loading
- Image Preprocessing
- Image Resizing (32 × 32)
- Feature Extraction (Flattening)
- Train-Test Split
- SVM Model Training
- Model Evaluation
- Prediction and Classification

🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- Scikit-learn
- Matplotlib

📋 Requirements

Install the required libraries:

pip install numpy opencv-python scikit-learn matplotlib

🤖 Machine Learning Model

Support Vector Machine (SVM)

The SVM algorithm is used to classify images into two categories: Cat and Dog. It creates an optimal decision boundary that helps distinguish between image features of both classes.

📊 Results

The trained model was evaluated on test data and achieved:

- Dataset Loaded: 2000 Images
- Accuracy Achieved: 56.0%

📁 Project Structure

Cats-vs-Dogs-Classification/
│
├── main.py
├── show_cat.py
├── show_dog.py
├── README.md
└── output_screenshot.png

🎯 Output

The model predicts whether the given input image belongs to a Cat or Dog class and displays the prediction result.
