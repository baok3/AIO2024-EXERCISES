import numpy as np

arr = np.arange(0 ,10)
arr[arr %2 ==1] = -1
print(arr)

# Output: [ 0 -1  2 -1  4 -1  6 -1  8 -1]
# Giải thích: lấy mảng arr, thay thế các phần tử lẻ bằng -1