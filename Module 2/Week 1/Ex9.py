import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10))
print("result", a[index])

# Giải thích:
# np.where((a >= 5) & (a <= 10)) trả về chỉ số của các phần tử trong a thỏa mãn điều kiện từ 5 đến 10
# a[index] lấy các phần tử tại các chỉ số trên