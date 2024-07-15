# Cách tạo một mảng boolean 3x3 với tất cả giá trị là True

import numpy as np

# a
arr_1 = np.ones((3, 3)) > 0

# b
arr_2 = np.ones((3, 3), dtype=bool)

# c
arr_3 = np.full((3, 3), fill_value=True, dtype=bool)

# d
# a,b,c đều đúng

# Đáp án đúng: d
# Giải thích: Cả 3 cách trên đều tạo mảng boolean 3x3 với tất cả giá trị là True.

# Cách 1 đúng vì np.ones((3, 3)) tạo mảng 3x3 với tất cả giá trị là 1, sau đó so sánh với 0 để tạo mảng boolean.
# Cách 2 đúng vì np.ones((3, 3), dtype=bool) tạo mảng 3x3 với tất cả giá trị là 1, với kiểu dữ liệu là boolean.
# Cách 3 đúng vì np.full((3, 3), fill_value=True, dtype=bool) tạo mảng 3x3 với tất cả giá trị là True, với kiểu dữ liệu là boolean.
