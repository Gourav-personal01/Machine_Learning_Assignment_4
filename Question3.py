# Q3. What is PCA (Principle Component Analysis), and how is it used in dimensionality reduction? Provide an
# example to illustrate its application.

# Answer - 
# Principal Component Analysis (PCA) is a dimensionality reduction technique used in machine learning and 
# statistics to reduce the number of features (dimensions) in a dataset while preserving as much of the original data's 
# variance as possible. PCA accomplishes this by transforming the original features into a new set of orthogonal features called 
# principal components. 

# Here's how PCA works in dimensionality reduction:

# Center the Data:

# Calculate the mean of each feature and subtract it from the corresponding feature values. This centers the data around the origin.
# Calculate the Covariance Matrix:

# Compute the covariance matrix of the centered data. The covariance matrix describes the relationships between features.

# Transform the Data:

# Use the selected eigenvectors to create a transformation matrix.