import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import linear_model, svm, neighbors, naive_bayes, tree, neural_network
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.decomposition import PCA

# Load data
cameras = pd.read_csv('clean_data.csv')

# Split into training and testing data
X = cameras.drop(columns=['Model', 'Brand', 'Price'])
y = cameras.Price

# PCA preprocessing
# pca = PCA(n_components=3)
# # components = pca.fit_transform(X[['Release date', 'Max resolution', 'Low resolution', 'Effective pixels', 'Zoom wide (W)', 'Zoom tele (T)', 'Normal focus range', 'Macro focus range', 'Storage included', 'Weight', 'Dimensions']])
# components = pca.fit_transform(X)
# print pca.explained_variance_ratio_
# X_train, X_test, y_train, y_test = train_test_split(components, y, test_size=0.3, random_state=42, shuffle=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)


reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)
prediction = reg.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print 'Linear Regression:'
print("MSE: %.4f" % mse)

ridge = linear_model.Ridge(alpha=0.5)
ridge.fit(X_train,y_train)
prediction = ridge.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print 'Ridge Regression:'
print("MSE: %.4f" % mse)

lasso = linear_model.Lasso(alpha = 0.1)
lasso.fit(X_train,y_train)
prediction = lasso.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print 'Lasso:'
print("MSE: %.4f" % mse)

knn = neighbors.KNeighborsRegressor(n_neighbors=6, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None)
knn.fit(X_train,y_train)
prediction = knn.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print 'K-Nearest Neighbors:'
print("MSE: %.4f" % mse)

n_bayes = naive_bayes.GaussianNB()
n_bayes.fit(X_train,y_train)
prediction = n_bayes.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print 'Naive Bayes:'
print("MSE: %.4f" % mse)

dec_tree = tree.DecisionTreeRegressor(max_depth=5)
dec_tree.fit(X_train,y_train)
prediction = dec_tree.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print 'Decision Tree:'
print("MSE: %.4f" % mse)

mlp = neural_network.MLPRegressor(hidden_layer_sizes=(25,15,8), activation='relu', solver='lbfgs', alpha=0.0001, batch_size='auto', learning_rate='adaptive', learning_rate_init=0.1, power_t=0.5, max_iter=400, shuffle=True, random_state=None, tol=0.00001, verbose=False, warm_start=True, momentum=0.6, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
mlp.fit(X_train,y_train)
prediction = mlp.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print 'Multi-Layer Perceptron:'
print("MSE: %.4f" % mse)


# #############################################################################
# GRADIENT BOOST
print 'Gradient Boost:'

# #############################################################################
# Fit regression model
lower_params = {'n_estimators': 200, 'learning_rate': 0.10, 'max_depth': 3, 'loss': 'quantile', 'alpha': 0.1,  'warm_start': True, 'verbose': 0}
params = {'n_estimators': 200, 'learning_rate': 0.10, 'max_depth': 3, 'loss': 'ls', 'warm_start': True, 'verbose': 0}
upper_params = {'n_estimators': 200, 'learning_rate': 0.10, 'max_depth': 3, 'loss': 'quantile', 'alpha': 0.9, 'warm_start': True, 'verbose': 0}

lower_boost = GradientBoostingRegressor(**lower_params)
boost = GradientBoostingRegressor(**params)
upper_boost = GradientBoostingRegressor(**upper_params)

lower_boost.fit(X_train, y_train)
boost.fit(X_train, y_train)
upper_boost.fit(X_train, y_train)

prediction = boost.predict(X_test)
mse = mean_squared_error(y_test, prediction)
print("MSE: %.4f" % mse)
print y_test.quantile([0,0.25,0.5,0.75,1])

# #############################################################################
# Plot training deviance
plot = False
if plot:
	# compute test set deviance
	test_score = np.zeros((params['n_estimators'],), dtype=np.float64)

	for i, y_pred in enumerate(boost.staged_predict(X_test)):
	    test_score[i] = boost.loss_(y_test, y_pred)

	plt.figure(figsize=(12, 6))
	plt.subplot(1, 2, 1)
	plt.title('Deviance')
	plt.plot(np.arange(params['n_estimators']) + 1, boost.train_score_, 'b-',
	         label='Training Set Deviance')
	plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
	         label='Test Set Deviance')
	plt.legend(loc='upper right')
	plt.xlabel('Boosting Iterations')
	plt.ylabel('Deviance')

	# #############################################################################
	# Plot feature importance
	feature_importance = boost.feature_importances_
	# make importances relative to max importance
	feature_importance = 100.0 * (feature_importance / feature_importance.max())
	sorted_idx = np.argsort(feature_importance)
	pos = np.arange(sorted_idx.shape[0]) + .5
	plt.subplot(1, 2, 2)
	plt.barh(pos, feature_importance[sorted_idx], align='center')
	plt.yticks(pos, X.columns[sorted_idx])
	plt.xlabel('Relative Importance')
	plt.title('Variable Importance')
	plt.show()

results = y_test.to_frame(name='True Price ($)')
results['Prediction ($)'] = prediction.round(2)
results.to_csv('model_results.csv', encoding='utf-8', index=False)


def encode_brand(brand):
	brand_dict = {'brand_Epson': 0, 'brand_Nikon': 0, 'brand_HP': 0, 'brand_Samsung': 0,
	'brand_Panasonic': 0, 'brand_Sigma': 0, 'brand_Sanyo': 0, 'brand_Agfa': 0, 'brand_JVC': 0,
	'brand_Olympus': 0, 'brand_Pentax': 0, 'brand_Kodak': 0, 'brand_Ricoh': 0, 'brand_Casio': 0,
	'brand_Contax': 0, 'brand_Toshiba': 0, 'brand_Sony': 0, 'brand_Fujifilm': 0, 'brand_Leica': 0,
	'brand_Canon': 0, 'brand_Kyocera': 0}

	brand_string = 'brand_' + brand
	if brand_string in brand_dict:
		brand_dict[brand_string] = 1
	else:
		print 'Error: Brand not found'
		return

	return brand_dict

def boost_predict(model,lower_model,upper_model,brand,date,max_res,low_res,pixels,zoom_w,zoom_t,normal_focus,macro_focus,storage,weight,dimensions):
	d = {'Release date' : date, 'Max resolution' : max_res, 'Low resolution': low_res, 'Effective pixels': pixels,
	'Zoom wide (W)': zoom_w, 'Zoom tele (T)': zoom_t, 'Normal focus range': normal_focus, 'Macro focus range': macro_focus,
	'Storage included': storage, 'Weight': weight, 'Dimensions' : dimensions}
	encoded_brand = encode_brand(brand)
	d.update(encoded_brand)
	X = pd.DataFrame(d, index=[0])

	y_lower = lower_model.predict(X)
	y = model.predict(X)
	y_upper = upper_model.predict(X)

	return y_lower, y, y_upper

lower_boost.fit(X, y)
boost.fit(X, y)
upper_boost.fit(X, y)
print boost_predict(boost,lower_boost,upper_boost,'Olympus',1997,1280,640.54,1,36,110,60,30,4,319,115)
