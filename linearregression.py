# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Dataset (Size, Price)
size = np.array([32.50234527, 53.42680403, 61.53035803, 47.47563963, 59.81320787, 55.14218841, 52.21179669,
                 39.29956669, 48.10504169, 52.55001444, 45.41973014, 54.35163488, 44.1640495, 58.16847072])
price = np.array([31.70700585, 68.77759598, 62.5623823, 71.54663223, 87.23092513, 78.21151827, 79.64197305,
                  59.17148932, 75.3312423, 71.30087989, 55.16567715, 82.47884676, 62.00892325, 75.39287043])

# Function to compute Mean Squared Error (MSE)
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Function to perform Gradient Descent
def gradient_descent(X, Y, m, c, learning_rate, epochs):
    n = len(X)
    for epoch in range(epochs):
        Y_pred = m * X + c  # Predicted value
        mse = mean_squared_error(Y, Y_pred)
        # Calculate gradients
        dm = (-2/n) * np.sum(X * (Y - Y_pred))  # Gradient for m (slope)
        dc = (-2/n) * np.sum(Y - Y_pred)        # Gradient for c (intercept)
        # Update weights
        m -= learning_rate * dm
        c -= learning_rate * dc
        print(f"Epoch {epoch+1}: MSE = {mse:.4f}")
    return m, c

# Random initial values for slope (m) and intercept (c)
m = np.random.randn()
c = np.random.randn()

# Hyperparameters
learning_rate = 0.0001
epochs = 10

# Training the model
m, c = gradient_descent(size, price, m, c, learning_rate, epochs)

# Plotting the line of best fit
plt.scatter(size, price, color='blue', label='Data points')
plt.plot(size, m * size + c, color='red', label='Best fit line')
plt.xlabel('Office Size')
plt.ylabel('Office Price')
plt.title('Office Size vs Price (Linear Regression)')
plt.legend()
plt.show()

# Predicting the price for an office size of 100 sq.ft
size_to_predict = 100
predicted_price = m * size_to_predict + c
print(f'Predicted price for 100 sq.ft office: {predicted_price}')
