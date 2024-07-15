import numpy as np

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print("Result", np.where(a < b, b, a))

# Giải thích:
# np.where(a < b, b, a) so sánh từng cặp phần tử của a và b, nếu phần tử của a nhỏ hơn b thì chọn phần tử từ b, ngược lại chọn từ a.