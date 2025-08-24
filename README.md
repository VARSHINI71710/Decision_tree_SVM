Iris Flower Classification using SVM
Task Description

Classify Iris flowers into three species — Setosa, Versicolor, Virginica — using a Support Vector Machine (SVM).

Dataset

Source: sklearn.datasets.load_iris()

Features: Sepal length, Sepal width, Petal length, Petal width

Target: Flower species (3 classes)

Total rows: 150

Steps Performed

Data Loading and Preprocessing

Loaded Iris dataset from sklearn.

Converted features and target to a DataFrame.

Scaled features using StandardScaler.

Model Training

Split data into train (80%) and test (20%) sets.

Trained SVM classifier with RBF kernel.

Evaluation

Calculated accuracy on the test set.

Plotted confusion matrix to check per-class performance.

Prediction

Predicted the species for new sample inputs.

Visualization

Pairplot for all features colored by species.

Decision boundary plot using first two features for 2D visualization.

Results

SVM achieved high accuracy in classifying Iris flowers.
Decision boundary shows clear separation between species in feature space.
Confusion matrix confirms correct classification for most samples.


Some data visualization:

<img width="565" height="455" alt="image" src="https://github.com/user-attachments/assets/3749afaf-1353-4949-87e6-088de4231ac9" />

<img width="1112" height="1023" alt="image" src="https://github.com/user-attachments/assets/b9b742ce-a852-44e5-a858-0b49e606255a" />

<img width="557" height="455" alt="image" src="https://github.com/user-attachments/assets/05c30226-3d43-4ee4-8258-40b5bc4c3694" />
