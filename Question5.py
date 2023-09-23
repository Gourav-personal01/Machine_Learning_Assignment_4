# Q5. You are working on a project to build a recommendation system for a food delivery service. The dataset
# contains features such as price, rating, and delivery time. Explain how you would use Min-Max scaling to
# preprocess the data.

import pandas as pd
df = pd.DataFrame({
    "price" : [177,188,189,292,299],
    "rating" : [1,2,3,4,5],
    "delivery_time" : [1,2,3,4,5]
})

print(df[['price']])

# currently the ranges are very large so we need to minimize without loose the shape then we will use min max scalling

from sklearn.preprocessing import MinMaxScaler

min_max = MinMaxScaler()
df_out = min_max.fit_transform(df[['price','rating','delivery_time']])
print(df_out)