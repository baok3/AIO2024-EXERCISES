def calc_se(y, y_hat):
    # Your code here
    return (y - y_hat)**2
    # End your code

y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))