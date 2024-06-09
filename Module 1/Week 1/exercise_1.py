'''Viết function thực hiện đánh giá classification model bằng F1-Score.
Input: function nhận 3 giá trị tp, fp, fn
Output: print ra kết quả của Precision, Recall, và F1-score'''

'''Đề bài yêu cầu các điều kiện sau: 
+ Phải kiểm tra giá trị nhận vào tp, fp, fn là type int, nếu là type khác thì print ví dụ
check fn là float, print ’fn must be int’ và thoát hàm hoặc dừng chương trình.
+ Yêu cầu tp, fp, fn phải đều lớn hơn 0, nếu không thì print ’tp and fp and fn must be
greater than zero’ và thoát hàm hoặc dừng chương trình.
'''

def exercise_1(tp, fp, fn):
    if type(tp) != int:
        print('tp phải là số nguyên')
        return
    if type(fp) != int:
        print('fp phải là số nguyên')
        return
    if type(fn) != int:
        print('fn phải là số nguyên')
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp và fp and fn phải lớn hơn 0')
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    print('Precision:', precision)
    print('Recall:', recall)
    print('F1-score:', f1)

