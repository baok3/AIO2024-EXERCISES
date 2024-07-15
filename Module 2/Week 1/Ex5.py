import numpy as np

arr = np.arange(10)
arr_2d = arr.reshape(2 ,-1)
print(arr_2d)

# Output: [[0 1 2 3 4]
#          [5 6 7 8 9]]
# Giải thích: tạo mảng arr, sau đó reshape thành mảng 2 chiều 2x5 (-1 tự động tính số cột)