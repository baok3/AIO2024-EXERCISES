'''Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện

Input: Một từ

Output: dictionary đếm số lần các chữ xuất hiện

Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]'''

def count_chars(string):
    result = {}

    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


if __name__ == '__main__':
    print(count_chars('smiles'))
