# Q4. What is the relationship between PCA and Feature Extraction, and how can PCA be used for Feature
# Extraction? Provide an example to illustrate this concept.

# Answer - 

# Principal Component Analysis (PCA) is a dimensionality reduction technique used in machine learning and 
# statistics to reduce the number of features (dimensions) in a dataset while preserving as much of the original data's 
# variance as possible.

# Feature Extraction - It is a Technique to get the important features to predict the data.

# Let's illustrate the concept of PCA as a feature extraction technique using a simple example:

# Suppose you have a dataset of grayscale images of handwritten digits (e.g., 28x28 pixel images of digits 0-9) for digit recognition. Each image has 784 pixels (28x28), resulting in 784 features for each image.

# To reduce the dimensionality of the data and extract meaningful features for digit recognition:

# Center the Data:

# Calculate the mean pixel value across all images and subtract this mean from each pixel value to center the data.
# Apply PCA:

# Perform PCA on the centered data. This involves calculating the covariance matrix, finding the eigenvalues and eigenvectors, and selecting the top N eigenvectors (principal components) that capture the most variance. Let's say you choose to retain the top 50 principal components.
# Transform the Data:

# Multiply each original image by the selected 50 principal components to obtain a reduced-dimensional representation of each image.