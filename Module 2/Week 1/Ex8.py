import numpy as np

arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))

# Giải thích:
# np.repeat(arr, 3) lặp lại từng phần tử của arr 3 lần
# np.tile(arr, 3) lặp lại toàn bộ arr 3 lần