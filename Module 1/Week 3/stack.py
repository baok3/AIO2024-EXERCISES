'''
Thực hiện xây dựng class Stack với các phương thức (method) sau đây:\

• initialization method nhận một input "capacity": dùng để khởi tạo stack với capacity là số lượng element mà stack có thể chứa

• .is_empty(): kiểm tra stack có đang rỗng

• .is_full(): kiểm tra stack đã full chưa

• .pop(): loại bỏ top element và trả về giá trị đó

• .push(value) add thêm value vào trong stack

• .top() lấy giá trị top element hiện tại của stack, nhưng không loại bỏ giá trị đó

• Không cần thiết phải thực hiện với pointer như trong hình minh họa

'''


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            return None

        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            return None

        self.stack.append(value)

    def top(self):
        if self.is_empty():
            return None

        return self.stack[-1]


# Example
stack1 = Stack(capacity=5)

stack1.push(1)

stack1.push(2)

print(stack1.is_full())

print(stack1.top())

print(stack1.pop())

print(stack1.top())

print(stack1.pop())

print(stack1.is_empty())

print()
