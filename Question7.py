# Q7. For a dataset containing the following values: [1, 5, 10, 15, 20], perform Min-Max scaling to transform the
# values to a range of -1 to 1.

import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create the dataset
data = np.array([1, 5, 10, 15, 20]).reshape(-1, 1)

# Create a MinMaxScaler instance
scaler = MinMaxScaler(feature_range=(-1, 1))

# Fit and transform the data using Min-Max scaling
scaled_data = scaler.fit_transform(data)

# Print the scaled data
print(scaled_data)
