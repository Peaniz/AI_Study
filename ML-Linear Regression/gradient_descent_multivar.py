import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

# get data
data = genfromtxt('advertising.csv', delimiter=',', skip_header=1)

# Lấy 3 features: TV, Radio, Newspaper
X = data[:, 0:3]
y = data[:, 3:4]  # Sales
N = data.shape[0]

# normalize data
maxi = np.max(X, axis=0)  # Lấy max theo từng cột
mini = np.min(X, axis=0)  # Lấy min theo từng cột
avg = np.mean(X, axis=0)  # Lấy mean theo từng cột
X = (X - avg) / (maxi - mini)

# Thêm cột 1 vào đầu X
X_b = np.c_[np.ones((N, 1)), X]

def batch_gradient_descent_multivar():
    epochs_max = 100
    learning_rate = 0.01
    
    # init theta (4 tham số: θ₀, θ₁, θ₂, θ₃)
    thetas = np.random.randn(4, 1)
    thetas_path = [thetas]
    losses = []
    
    for i in range(epochs_max):
        # predict y_hat = θ₀ + θ₁x₁ + θ₂x₂ + θ₃x₃
        y_hat = X_b.dot(thetas)
        
        # compute loss (MSE)
        loss = (y_hat - y) ** 2
        mean_loss = np.sum(loss) / N
        losses.append(mean_loss)
        
        # compute gradients
        gradients = 2 * X_b.T.dot(y_hat - y) / N
        
        # update parameters
        thetas = thetas - learning_rate * gradients
        thetas_path.append(thetas)
        
        # In ra loss sau mỗi 10 epochs
        if i % 10 == 0:
            print(f"Epoch {i}, Loss: {mean_loss:.4f}")
    
    return thetas_path, losses

# Train mô hình
bgd_thetas, losses = batch_gradient_descent_multivar()

# In ra các hệ số hồi quy cuối cùng
print("\nHệ số hồi quy tìm được:")
print(f"θ₀ (bias): {bgd_thetas[-1][0][0]:.4f}")
print(f"θ₁ (TV): {bgd_thetas[-1][1][0]:.4f}")
print(f"θ₂ (Radio): {bgd_thetas[-1][2][0]:.4f}")
print(f"θ₃ (Newspaper): {bgd_thetas[-1][3][0]:.4f}")

# Vẽ đồ thị loss function
plt.figure(figsize=(10, 6))
plt.plot(range(len(losses)), losses, 'b-')
plt.title('Loss Function over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Mean Squared Error')
plt.grid(True)
plt.show()

# Dự đoán và tính R-squared
y_pred = X_b.dot(bgd_thetas[-1])
r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)
print(f"\nR-squared score: {r2:.4f}")

# Vẽ scatter plot của giá trị thực tế và dự đoán
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, color='blue', alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.grid(True)
plt.show()
