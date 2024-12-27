import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
# get data
data = genfromtxt('advertising.csv', delimiter=',', skip_header=1)

X = data[:, 0:1]
print()

y = data[:, 3:4]
print(y)
N = data.shape[0]

# normalize data
maxi = np.max(X)
mini = np.min(X)
avg = np.mean(X)
X = (X-avg) / (maxi-mini)

# get X bar [1,X]
X_b = np.c_[np.ones((N, 1)), X]



def batch_gradient_descent():
    epochs_max = 100
    learning_rate = 0.01

    # init theta
    thetas = np.random.randn(2, 1)
    thetas_path = [thetas]
    losses = []

    for i in range(epochs_max):
        # predict y_hat
        y_hat = X_b.dot(thetas)

        # compute loss
        loss = (y_hat - y) ** 2

        # compute gradient for loss
        d_loss = 2 * (y_hat - y) / N

        # compute gradient for params
        gradients = X_b.T.dot(d_loss)

        # update
        thetas = thetas - learning_rate * gradients
        thetas_path.append(thetas)

        mean_loss = np.sum(loss) / N
        losses.append(mean_loss)

    return thetas_path, losses


bgd_thetas, losses = batch_gradient_descent()

print(bgd_thetas[-1])

# in loss cho 100 sample đầu
x_axis = list(range(100))
plt.plot(x_axis, losses[:100], color="r")
plt.show()

plt.figure(figsize=(10,5))

# Plot 1: Loss function
plt.subplot(1,2,1)
plt.plot(x_axis, losses[:100], color="r")
plt.title('Loss Function')
plt.xlabel('Epochs')
plt.ylabel('Loss')

# Plot 2: Regression Line
plt.subplot(1,2,2)
X_orig = data[:, 0:1]  # Dữ liệu X gốc chưa normalize
y_orig = data[:, 3:4]  # Dữ liệu y 
plt.scatter(X_orig, y_orig)

# Vẽ đường hồi quy
X_test = np.linspace(X_orig.min(), X_orig.max(), 100).reshape(-1,1)
X_test_norm = (X_test - avg) / (maxi-mini)
X_test_b = np.c_[np.ones((100,1)), X_test_norm]
y_pred = X_test_b.dot(bgd_thetas[-1])
plt.plot(X_test, y_pred, color='r', linewidth=2)

plt.title('Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.show()