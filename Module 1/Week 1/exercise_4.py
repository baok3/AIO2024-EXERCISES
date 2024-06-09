import math
def calc_sig(x):
    # Your code here
    return 1/(1 + math.exp(-x))
    # End your code

assert round ( calc_sig (3) , 2) ==0.95
print (round(calc_sig (2), 2))
