import numpy as np
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)

print("C = ", c)

# Giải thích :
# arr1 = np.arange(10).reshape(2, -1) tạo một mảng từ 0 đến 9 và định hình lại thành mảng 2 hàng, mỗi hàng có 5 phần tử

# arr2 = np.repeat(1, 10).reshape(2, -1) tạo một mảng có 10 phần tử đều là 1 và định hình lại thành mảng 2 hàng, mỗi hàng có 5 phần tử

# c = np.concatenate([arr1, arr2], axis=1) nối arr1 và arr2 theo trục 1 (trục cột)