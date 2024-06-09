import math

def approx_sin(x, n):
    # Your code here
    sin = 0
    for i in range(n):
        sin += ((-1)**i) * (x**(2*i + 1)) / math.factorial(2*i + 1)
    return sin
    # End your code

assert round(approx_sin(x = 1, n = 10), 4) == 0.8415
print(round(approx_sin(x = 3.14, n = 10), 4))
