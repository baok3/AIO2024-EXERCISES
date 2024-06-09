import math

# Công thức chính xác của MD_nRE
def md_nre(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = abs(y_root - y_hat_root)
    loss = difference ** p
    return loss

# Các hàm được đưa ra
def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

def md_nre_single_sample1(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / 2)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

def md_nre_single_sample2(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root / y_hat_root
    loss = difference ** p
    return loss

def md_nre_single_sample3(y, y_hat, n, p):
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    difference = y_root - y_hat_root
    loss = difference
    return loss

# Hàm kiểm tra
def check_md_nre_functions(y, y_hat, n, p):
    correct_value = md_nre(y, y_hat, n, p)
    
    if math.isclose(md_nre_single_sample(y, y_hat, n, p), correct_value, rel_tol=1e-9):
        print("Hàm (A) đúng.")
    else:
        print("Hàm (A) sai.")
    
    if math.isclose(md_nre_single_sample1(y, y_hat, n, p), correct_value, rel_tol=1e-9):
        print("Hàm (B) đúng.")
    else:
        print("Hàm (B) sai.")
    
    if math.isclose(md_nre_single_sample2(y, y_hat, n, p), correct_value, rel_tol=1e-9):
        print("Hàm (C) đúng.")
    else:
        print("Hàm (C) sai.")
    
    if math.isclose(md_nre_single_sample3(y, y_hat, n, p), correct_value, rel_tol=1e-9):
        print("Hàm (D) đúng.")
    else:
        print("Hàm (D) sai.")

# Kiểm tra với các giá trị mẫu
y = 100
y_hat = 99.5
n = 2
p = 2

check_md_nre_functions(y, y_hat, n, p)