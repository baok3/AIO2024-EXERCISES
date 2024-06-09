def calc_ae(y, y_hat):
    # Your code here
    # abs : absolute value (giá trị tuyệt đối)
    return abs(y - y_hat)
    # End your code

y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))