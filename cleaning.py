import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AffinityPropagation

cameras = pd.read_csv('camera_dataset.csv')

def get_brand(row):
	return row.Model.partition(' ')[0]

# Rename weight column
new_columns = cameras.columns.values
new_columns[-3] = 'Weight'
cameras.columns = new_columns

# Include brand column
cameras['Brand'] = cameras.apply(get_brand,axis=1)
cameras = cameras[['Model', 'Brand', 'Release date', 'Max resolution', 'Low resolution', 'Effective pixels', 'Zoom wide (W)', 'Zoom tele (T)', 'Normal focus range', 'Macro focus range', 'Storage included', 'Weight', 'Dimensions', 'Price']]

# Check for missing data - looks like there are just two entries with missing values
old = cameras.shape
cameras.dropna(inplace=True)

# Remove super expensive cameras
# cameras = cameras[cameras.Price > 100]

# Replace sketchy zero values with mean
mean_weight = cameras['Weight'].mean()
mean_dimension = cameras['Dimensions'].mean()

cameras.Weight.replace(0, mean_weight, inplace=True)
cameras.Dimensions.replace(0, mean_dimension, inplace=True)

# Use one-hot encoding to turn brands into categories
cameras = pd.concat([cameras,pd.get_dummies(cameras['Brand'], prefix='brand')],axis=1)

# Cluster data
kmeans = KMeans(n_clusters=7, random_state=0).fit(cameras.drop(['Price', 'Model','Brand'],axis=1))
# kmeans = KMeans(n_clusters=7, random_state=0).fit(cameras[['Zoom tele (T)', 'Weight']])
# kmeans = KMeans(n_clusters=7, random_state=0).fit(cameras[['Weight', 'Max resolution', 'Zoom tele (T)']])
# cameras['cluster']=kmeans.labels_

# Scale data
# NOTE: If we train on scaled data, wouldn't that mean we need to scale inputs to prediction in the same way? How would that work?
# scaler = StandardScaler()
# cameras[['Release date', 'Max resolution', 'Low resolution', 'Effective pixels', 'Zoom wide (W)', 'Zoom tele (T)', 'Normal focus range', 'Macro focus range', 'Storage included', 'Weight', 'Dimensions']] = scaler.fit_transform(cameras[['Release date', 'Max resolution', 'Low resolution', 'Effective pixels', 'Zoom wide (W)', 'Zoom tele (T)', 'Normal focus range', 'Macro focus range', 'Storage included', 'Weight', 'Dimensions']])

# Export final dataframe to csv
cameras.to_csv('clean_data.csv', encoding='utf-8', index=False)
print 'Cleaning complete'
