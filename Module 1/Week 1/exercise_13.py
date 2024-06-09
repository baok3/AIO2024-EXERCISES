"""Đoạn code nào thực hiện đúng Mean Difference of n^th Root Error được miêu tả ở trên?"""

# câu A
def md_nre_single_sample (y , y_hat , n , p) :
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/ n )
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

# câu B
def md_nre_single_sample1 (y , y_hat , n , p ) :
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/2) # Sử dụng căn bậc 2 thay vì căn bậc n
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

# câu C
def md_nre_single_sample2 (y , y_hat , n , p ) :
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/ n )
    difference = y_root / y_hat_root # Sử dụng phép chia thay vì phép trừ
    loss = difference ** p
    return loss

# Câu D
def md_nre_single_sample3 (y , y_hat , n , p ) :
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/ n )
    difference = y_root - y_hat_root
    loss = difference # Không nâng lũy thừa p
    return loss

y = 100
y_hat = 99.5
n = 2
p = 1

def real_md_nre(y, y_hat, n, p):
    y_root = y ** (1/ n )
    y_hat_root = y_hat ** (1/ n )
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

print(real_md_nre(y, y_hat, n, p))

def compare_md_nre(y, y_hat, n, p):
    if md_nre_single_sample(y, y_hat, n, p) == real_md_nre(y, y_hat, n, p):
        print("Câu A Đúng")
    elif md_nre_single_sample1(y, y_hat, n, p) == real_md_nre(y, y_hat, n, p):
        print("Câu B Đúng")  
    elif md_nre_single_sample2(y, y_hat, n, p) == real_md_nre(y, y_hat, n, p):
        print("Câu C Đúng")
    elif md_nre_single_sample3(y, y_hat, n, p) == real_md_nre(y, y_hat, n, p):
        print("Câu D Đúng")

compare_md_nre(y, y_hat, n, p)



