# Trong pytorch, torch.nn.Module là lớp cơ bản để từ đó xây dựng lên các mô hình hoặc các phương
# thức kích hoạt (activation funtion) như sigmoid, softmax,... Trong phần này, chúng ta xây dựng
# class Softmax và softmax_stable nhận đầu vào là mảng 1 chiều (tensor 1 chiều) dựa vào kế thừa
# từ lớp Module và ghi đè vào phương thức forward() theo công thức sau đây:

# softmax(x)_i = exp(x_i) / sum(exp(x_j)) với i = 1, 2, ..., n

# softmax_stable(x)_i = exp(x_i - max(x)) / sum(exp(x_j - max(x))) với i = 1, 2, ..., n

import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        # pylint: disable=no-member
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        # pylint: disable=no-member
        return torch.exp(x - torch.max(x)) / torch.sum(torch.exp(x - torch.max(x)), dim=0)


# Example 1
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

# Example 2
data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
