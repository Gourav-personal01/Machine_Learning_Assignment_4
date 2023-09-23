# Q1. What is Min-Max scaling, and how is it used in data preprocessing? Provide an example to illustrate its
# application.

# Answer - 

# MinMax Scaler shrinks the data within the given range, usually of 0 to 1. It transforms data by scaling features to a given range. 
# It scales the values to a specific value range without changing the shape of the original distribution

import seaborn as sns
import pandas as pd

df = sns.load_dataset('taxis')

print(df[['distance','fare','tip']])

from sklearn.preprocessing import MinMaxScaler

min_max = MinMaxScaler()

df_out = min_max.fit_transform(df[['distance','fare','tip']])

print(df_out)
