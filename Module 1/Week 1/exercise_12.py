import math

def approx_cosh(x, n):
    # Your code here
    cosh = 0
    for i in range(n):
        cosh += (x**(2*i)) / math.factorial(2*i)
    return cosh
    # End your code

assert round(approx_cosh(x = 1, n = 10), 2) == 1.54
print(round(approx_cosh(x = 3.14, n = 10), 2))