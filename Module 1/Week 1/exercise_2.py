def is_number(n):
    """Viết function is_number nhận input có thể là string hoặc một số kiểm tra n (một số) có hợp lệ hay không (vd: n=’10’, is_number(n) sẽ trả về True ngược lại là False). 
    Đầu ra của chương trình sau đây là gì?"""
 # Your code here
    try:
        float(n)
        return True
    except ValueError:
        return False
 # End your code

assert is_number (3) == 1.0
assert is_number (' -2a') == 0.0
print ( is_number (1) )
print ( is_number ('n') )