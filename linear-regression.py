import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Generating Random Dataset
np.random.seed(42)
x = np.random.rand(50,1)*100
y = 3.5 * x + np.random.rand(50,1)*20

#Creating and Training Linear Regression Model
model = LinearRegression()
model.fit(x,y)

#Predicting Y Values
y_predict = model.predict(x)

#Visualizing the Regression Line
plt.figure(figsize=(8,6)) 
plt.scatter(x, y, color='blue', label='Data Points') 
plt.plot(x, y_predict, color='red', linewidth=2, label='Regression Line') 
plt.title('Linear Regression on Random Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

#Slope and Intercept
print("Slope (Coefficient):", model.coef_[0][0])
print("Intercept:", model.intercept_[0])