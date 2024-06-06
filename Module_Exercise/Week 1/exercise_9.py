import math

def approx_cos(x, n):
    # Your code here
    cos = 0
    for i in range(n):
        cos += ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    return cos
    # End your code

assert round(approx_cos(x =1, n=10), 2) == 0.54
print(round(approx_cos(x = 3.14, n = 10), 2))