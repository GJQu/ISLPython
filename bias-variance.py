import numpy as np
import matplotlib.pyplot as plt

# Simulate model flexibility
flexibility = np.linspace(1, 100, 400)

# Squared Bias - decreases with flexibility
squared_bias = 1 / (flexibility**0.5)

# Variance - increases with flexibility
variance = flexibility**0.5 / 100

# Training Error - U-shaped curve
training_error = squared_bias * (1 - np.log(flexibility) / np.log(100))

# Test Error - U-shaped curve, but higher than training error
test_error = training_error + variance

# Bayes (Irreducible) Error - constant
bayes_error = np.full_like(flexibility, 0.2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(flexibility, squared_bias, label='Squared Bias')
plt.plot(flexibility, variance, label='Variance')
plt.plot(flexibility, training_error, label='Training Error')
plt.plot(flexibility, test_error, label='Test Error')
plt.plot(flexibility, bayes_error, label='Bayes Error', linestyle='--')

plt.xlabel('Model Flexibility')
plt.ylabel('Error')
plt.title('Bias-Variance Tradeoff')
plt.legend()
plt.grid(True)
plt.show()
