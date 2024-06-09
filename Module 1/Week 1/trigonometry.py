'''Viết 4 functions để ước lượng các hàm số sau:
hàm sin(x), hàm cos(x), hàm sinh(x), hàm cosh(x)
Input: x (số muốn tính toán) và n (số lần lặp muốn xấp xỉ)

Output: Kết quả ước lượng hàm tương ứng với x. 

chú ý các điều kiện sau:
+ x là radian
+ n là số nguyên dương > 0
+ các bạn nên viết một hàm tính giai thừa riêng'''

def đạo_hàm(n):
    if n == 0:
        return 1
    return n * đạo_hàm(n - 1)

def hàm_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / đạo_hàm(2 * i + 1)
    return result

def hàm_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / đạo_hàm(2 * i)
    return result

def hàm_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / đạo_hàm(2 * i + 1)
    return result

def hàm_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / đạo_hàm(2 * i)
    return result

if __name__ == '__main__':
    x = float(input('Nhập x: '))
    n = int(input('Nhập n: '))
    print('sin(x) =', hàm_sin(x, n))
    print('cos(x) =', hàm_cos(x, n))
    print('sinh(x) =', hàm_sinh(x, n))
    print('cosh(x) =', hàm_cosh(x, n))
