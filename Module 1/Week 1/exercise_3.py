'''Viết function lựa chọn regression loss function để tính loss:

Input:
+ Người dùng nhập số lượng sample (num_samples) được tạo ra (chỉ nhận integer numbers)
+ Người dùng nhập loss name (MAE, MSE, RMSE-(optional)) chỉ cần MAE và MSE, bạn nào muốn làm thêm RMSE đều được.

Output: Print ra loss name, sample, predict, target, loss
+ loss name: là loss mà người dùng chọn
+ sample: là thứ tự sample được tạo ra (ví dụ num_samples=5, thì sẽ có 5 samples và mỗi sample là sample-0, sample-1, sample-2, sample-3, sample-4)
+ predict: là số mà model dự đoán (chỉ cần dùng random tạo random một số trong range[0,10))
+ target: là số target mà momg muốn mode dự đoán đúng (chỉ cần dùng random tạo random một số trong range [0,10))
+ loss: là kết quả khi đưa predict và target vào hàm loss
+ note: ví dụ num_sample=5 thì sẽ có 5 cặp predict và target.'''

import random

def exercise_3(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('num_samples phải là số nguyên')
        return
    if loss_name not in ['MAE', 'MSE', 'RMSE']:
        print('loss_name không hợp lệ')
        return
    for i in range(num_samples):
        predict = random.randint(0, 10)
        target = random.randint(0, 10)
        if loss_name == 'MAE':
            loss = abs(predict - target)
        elif loss_name == 'MSE':
            loss = (predict - target) ** 2
        else:
            loss = ((predict - target) ** 2) ** 0.5
        print('------------------')
        print('loss name:', loss_name)
        print('sample:', f'sample-{i}')
        print('predict:', predict)
        print('target:', target)
        print('loss:', loss)

if __name__ == '__main__':
    num_samples = int(input('Nhập num_samples: '))
    loss_name = input('Nhập loss_name: ')
    exercise_3(num_samples, loss_name)


