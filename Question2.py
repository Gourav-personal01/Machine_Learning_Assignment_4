# Q2. What is the Unit Vector technique in feature scaling, and how does it differ from Min-Max scaling?
# Provide an example to illustrate its application.

# Answer - 
# 1. Unit Vector (Normalization):
# Normalization scales the features in such a way that they are transformed to a common scale, resulting in a unit 
# vector length (i.e., a vector with a length or magnitude of 1). 

# 2. Min-Max Scaling (Rescaling):
# Min-Max scaling, also known as Rescaling or Min-Max normalization, scales the features to a specific range, typically between 0 and 1. This technique transforms the feature values so that the minimum value becomes 0, 
# the maximum value becomes 1, and all other values are linearly scaled within this range.

import seaborn as sns

df = sns.load_dataset('iris')

print(df.head())

from sklearn.preprocessing import normalize

print(df.columns)

normalize_value = normalize(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width',]])

print(normalize_value)