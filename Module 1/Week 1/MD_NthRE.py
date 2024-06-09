'''Viết function thực hiện Mean Difference of n^th Root Error:

Input: y (giá trị của y), y_hat (gía trị của yˆ), n (căn bậc n), và p (bậc của hàm loss)

Output: Kết quả của hàm loss
'''

def MD_NthRE(y, y_hat, n, p):
    return (y**(1/n) - y_hat**(1/n))**p

if __name__ == '__main__':
    y = float(input('Nhập y: '))
    y_hat = float(input('Nhập y_hat: '))
    n = int(input('Nhập n: '))
    p = int(input('Nhập p: '))
    print('Mean Difference of nth Root Error =', mean_difference_of_nth_root_error(y, y_hat, n, p))
