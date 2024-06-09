'''Viết function mô phỏng theo 3 activation function.

Input:
+ Người dùng nhập giá trị x
+ Người dùng nhập tên activation function chỉ có 3 loại (sigmoid, relu, elu)

Output: Kết quả f(x) (x khi đi qua activation function tương ứng theo activation function
name).

Lưu ý các điều kiện sau:
+ Dùng function is_number được cung cấp sẵn để kiểm tra x có hợp lệ hay không
+ Kiểm tra activation function name có hợp lệ hay không nằm trong 3 tên (sigmoid, relu, elu). Nếu không print ’ten_function_user is not supported’
+ Convert x sang float type
+ Thực hiện theo công thức với activation name tương ứng. Print ra kết quả
+ Dùng math.e để lấy số e
+ α = 0.01'''

import math

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return 'x phải là số nguyên hoặc số thực'

def activation_function(x, activation_name):
    if activation_name not in ['sigmoid', 'relu', 'elu']:
        print('chương trình không hỗ trợ hàm này')
        return
    if not is_number(x):
        print('x phải là số nguyên hoặc số thực')
        return
    x = float(x)
    if activation_name == 'sigmoid':
        result = 1 / (1 + math.e ** -x)
    elif activation_name == 'relu':
        result = max(0, x)
    else:
        result = x if x > 0 else 0.01 * (math.e ** x - 1)
    print(result)

