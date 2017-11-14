# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler() 
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()




import coremltools

coreml_model = coremltools.converters.sklearn.convert(regressor,
                                                         "Experience",
                                                         "Salary")
coreml_model.author = "Juber Moulvi Abdul"
coreml_model.short_description = "I approximate a salary based on experience with a linear model!"  

# Set model metadata
coreml_model.author = 'Juber Moulvi Abdul'
coreml_model.license = 'Opteamix LLC'

# Set feature descriptions manually
coreml_model.short_description = 'Predicts the salary of a person in the based on experience.'
coreml_model.input_description["Experience"] = "A real number"  


# Set the output descriptions
coreml_model.output_description["Salary"] = "Predicted salary."

# Save the model
coreml_model.save('SalaryPrediction.mlmodel')



