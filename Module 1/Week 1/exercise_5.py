import math

def calc_elu(x):
    # Your code here
    alpha = 0.01
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x

    # End your code

assert round ( calc_elu (1)) == 1
print(round(calc_elu(-1),2))

# x = -1 vì x <= 0 nên 0.01 * (e^-1 - 1) = 0.01 * (1/e - 1) = 0.01 * (1/2.718 - 1) = 0.01 * (0.367 - 1) = 0.01 * (-0.633) = -0.00633 = -0.01 (làm tròn 2 chữ số thập phân)