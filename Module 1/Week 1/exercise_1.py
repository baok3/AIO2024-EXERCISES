import math

def calc_f1_score(tp ,fp ,fn) -> float:
    """Câu hỏi 1 : Viết function thực hiện đánh giá classification model bằng F1-Score. 
        Function nhận vào 3 giá trị tp, fp, fn và trả về F1-score."""

    # Your code here
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)
    return f1_score
    # End your code

assert round (calc_f1_score(tp =2 ,fp =3 ,fn =5) ,2) >= 0.33
print(round(calc_f1_score(tp =2 ,fp =4 ,fn =5),2))