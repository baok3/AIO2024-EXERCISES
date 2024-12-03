import torch
import numpy as np
import pandas as pd
from  torch import nn
from torch import optim
from datetime import datetime
from torchmetrics import Accuracy
from torch.utils.data import Dataset

'''
+ Chức năng : Kiểm tra ký tự nhập vào có phải là chữ cái thường không
hay là khoảng trắng không.

Ghi chú : Assign class như trong file yaml config từ 0 trở đi tương ứng
với phím trên bàn phím. Như 'a' tương ứng với 0, 'b' tương ứng với 1, ...
'''

def is_handsign_character(char:str):
    return ord('a') <= ord(char) <= ord('q') or char == " "

'''
Đọc file yaml (hand_gesture) và trả về một dictionary chứa các nhãn (cử chỉ)
với mục đích là sử dụng các label này để gắn nhãn cho dữ liệu thu thập.
'''

def label_dict_from_config(relative_path):
    with open(relative_path, "r") as f:
        label_tag = yaml.full_load(f)["gestures"]
    return label_tag

'''
Ghi dữ liệu (landmark) và label vào file csv
__init__ : Mở file csv để ghi dữ liệu
add : Thêm dữ liệu vào file csv bao gồm nhãn và tọa độ
close : Đóng file csv sau khi hoàn tất
'''

class HandDatasetWriter():
    def __init__(self, filepath) -> None:
        self.csv_file = open(filepath, "a")
        self.file_writer = csv.writer(self.csv_file, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    def add(self, hand, label):
        self.file_writer.writerow([label, *np.array(hand).flatten().tolist()])
    def close(self):
        self.csv_file.close()

'''
Phát hiện bàn tay trong khung và trích xuất các landmark
__init__ : Khởi tạo thành phần cần thiết của Mediapipe để nhận diện bàn tay
detetctHand :
- Chuyển đổi frame từ BGR sang RGB.
- Sử dụng mediapipe để nhận diện bàn tay và trích xuất các landmark.
- Trả về danh sách các landmark và hình ảnh đã vẽ.
'''

class HandLandmarkDetector():
    def __init__(self) -> None:
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.detector = self.mp_hands.Hands(False, max_num_hands=1, 
                                            min_detection_confidence=0.5)
        
    def detectHand(self, frame):
        hands = []
        frame = cv2.flip(frame, 1)
        annotated_image = frame.copy()
        result = self.detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if result.multi_hand_landmarks is not None:
            for hand_landmarks in result.multi_hand_landmarks:
                hand = []
                self.mp_drawing.draw_landmarks(
                    annotated_image, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
                for landmark in hand_landmarks.landmark:
                    x,y,z = landmark.x, landmark.y, landmark.z
                    hand.extend([x,y,z])
            hands.append(hand)
        return hands, annotated_image
    

# Vòng lặp chính để thu thập dữ liệu cử chỉ
def run(data_path, sign_img_path, split = "val", resolution = (1280, 720)):
    '''
    Parameters :
    - data_path : Đường dẫn lưu dữ liệu CSV
    - sign_img_path : Đường dẫn lưu hình ảnh cử chỉ
    - split : Phân loại dữ liệu (train, val, test)
    - resolution : Độ phân giải của webcam
    Flow : 
    - Khởi tạo HandLandmarkDetector() để nhận diện và mở cam
    - Tạo các thư mục cần thiết
    - Vòng lặp chính :
        + Đọc frame từ cam
        + Nhận diện bàn tay và trích xuất landmark
        + Xử lý trạng thái ghi dữ liệu dựa trên phím bấm
        + Ghi dữ liệu khi cần thiết
        + Hiển thị thông tin lên màn hình
    '''
    hand_detector = HandLandmarkDetector()
    cam = cv2.VideoCapture(0)
    cam.set(3, resolution[0])
    cam.set(4, resolution[1])
    os.makedirs(data_path, exist_ok=True)
    os.makedirs(sign_img_path, exist_ok=True)
    print(sign_img_path)
    dataset_path = f"./{data_path}/landmark_{split}.csv"
    hand_dataset = HandDatasetWriter(dataset_path)
    current_letter = None
    status_text = None
    cannot_swith_char = False

    saved_frame = None
    while cam.isOpened():
        _, frame = cam.read()
        hands, annotated_image = hand_detector.detectHand(frame)

        if (current_letter is None):
            status_text = "Press a to start recording"
        else:
            label = ord(current_letter) - ord('a')
            if label == -65:
                status_text = f"Recording unknown, press space to stop"
                label = -1
            else:
                status_text = f"Recording {LABEL_TAG[label]}, press {current_letter} again to stop"
        
        key = cv2.waitKey(1)
        if (key == -1):
            if (current_letter is None):
                pass
            else:
                if len(hands) != 0:
                    hand = hands[0]
                    hand_dataset.add(hand=hand, label=label)
                    saved_frame = frame

        else:
            key = chr(key)
            if key == 'q':
                break
            if (is_handsign_character(key)):
                if (current_letter is None):
                    current_letter = key
                elif (current_letter == key):
                    if saved_frame is not None:
                        if label >= 0:
                            cv2.imwrite(f"./{sign_img_path}/{LABEL_TAG[label]}.jpg", saved_frame)
                        cannot_swith_char = False
                        current_letter = None
                        saved_frame = None
                else:
                    cannot_swith_char = True
        if cannot_swith_char:
            cv2.putText(annotated_image, f"please press {current_letter} again to stop unbind",
                        (0, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(annotated_image, status_text, (5, 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow(f"{split}", annotated_image)
    cv2.destroyAllWindows()

# Điểm bắt đầu của chương trình
if __name__ == "__main__":
    '''
    Flow :
    - Đọc class từ file yaml
    - Thiếp lập đường dẫn lưu dữ liệu và hình ảnh
    - Gọi run 3 lần để xây dựng dữ liệu train, val, test
    '''
    LABEL_TAG = label_dict_from_config("hand_gesture.yaml")
    data_path = "./data2"
    sign_img_path = "./sign_img2"
    run(data_path, sign_img_path, "train", (1280, 720))
    run(data_path, sign_img_path, "val", (1280, 720))
    run(data_path, sign_img_path, "test", (1280, 720))