import numpy as np


# Định nghĩa hàm f(x)
def f(x):
    return (np.exp(-x) - 4 / np.exp(x)) ** 2


# Định nghĩa đạo hàm của f(x) (thêm giới hạn cho x để tránh overflow)
def df(x):
    # Giới hạn giá trị của x để tránh tràn số
    if x > 100:
        x = 100
    elif x < -100:
        x = -100
    return -4 * np.exp(-2 * x) + 8 * np.exp(-x) - 16 * np.exp(x) + 32 / np.exp(2 * x)


# Thuật toán Gradient Descent with Momentum
def gradient_descent_momentum(learning_rate, beta, max_iter, tol):
    x = 0.0  # Khởi tạo điểm ban đầu
    v = 0.0  # Khởi tạo vận tốc (momentum)

    for i in range(max_iter):
        grad = df(x)  # Tính gradient
        v = beta * v + learning_rate * grad  # Cập nhật vận tốc
        x_new = x - v  # Cập nhật vị trí mới

        # Kiểm tra điều kiện hội tụ
        if np.abs(x_new - x) < tol:
            break

        x = x_new

    return x, f(x)


# Tham số thuật toán
learning_rate = 0.01
beta = 0.9
max_iter = 1000
tol = 1e-6

# Chạy thuật toán
x_opt, f_max = gradient_descent_momentum(learning_rate, beta, max_iter, tol)
print(f"Giá trị x tại điểm cực đại: {x_opt}")
print(f"Giá trị lớn nhất của hàm f(x): {f_max}")
