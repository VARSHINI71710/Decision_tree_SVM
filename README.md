🌸 Iris Flower Classification using SVM

Iris flower classification Streamlit link: Click Here

📝 Task Description

This project classifies Iris flowers into three species — Setosa 🌼, Versicolor 🌸, Virginica 🌺 — using a Support Vector Machine (SVM) classifier.

Goal: Predict the species of an Iris flower based on its sepal and petal measurements.

📊 Features

Sepal length (cm)

Sepal width (cm)

Petal length (cm)

Petal width (cm)

Target: Flower species (3 classes: Setosa, Versicolor, Virginica)
Total rows: 150

⚡ Steps Performed
1️⃣ Data Loading and Preprocessing

Loaded the Iris dataset from sklearn.datasets.

Converted features and target into a Pandas DataFrame for better handling.

Encoded the target species using LabelEncoder.

Scaled features using StandardScaler to standardize input for SVM.

2️⃣ Model Training

Split the dataset into train (80%) and test (20%) sets.

Trained an SVM classifier with RBF kernel on scaled training data.

3️⃣ Model Evaluation

Predicted species on the test set.

Calculated accuracy to measure performance.

Plotted confusion matrix to check per-class performance.

4️⃣ Prediction

Tested the trained model with new sample inputs.

Model predicts the species based on user-provided sepal and petal measurements.

5️⃣ Visualization

Pairplot: Visualizes feature relationships colored by species.

Decision boundary plot: Shows separation between species using the first two features in 2D.

🎯 Results

The SVM model achieved high accuracy in classifying Iris flowers.

Decision boundary clearly separates species in feature space.

Confusion matrix confirms correct classification for most samples.

🛠 Tools and Libraries

Python 3.12.5

scikit-learn (SVM, dataset, preprocessing, metrics)

Pandas and NumPy

Matplotlib and Seaborn (visualizations)

Streamlit (for interactive predictions)
