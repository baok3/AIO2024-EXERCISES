import numpy as np

arr = np.arange(0 ,10)

print (arr[arr %2 == 1])

# [1 3 5 7 9] vì array lấy các phần tử có giá trị lẻ hoặc không chia hết cho 2