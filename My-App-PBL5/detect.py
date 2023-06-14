import cv2
import torch
import numpy as np
from skimage import measure
import os
from cvzone import SerialModule
import pandas as pd

model = torch.hub.load('ultralytics/yolov5', 'custom', path='E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/weights/best.pt')

# Xuất ra ma trận nhị phân ( đen = 0, trắng = 255)
def feature(folder_path, file):
    binaries = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            # Đọc tệp tin ảnh
            img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)

            # Đổi ảnh sang ma trận nhị phân
            ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

            # Thêm ma trận nhị phân vào mảng
            binaries.append(binary)
        

    # Khởi tạo mảng pixel trắng đen có kích thước giống với các ma trận trong binaries với các phần tử được khởi tạo là 0
    black_pixels = np.zeros_like(binaries[0])
    white_pixels = np.zeros_like(binaries[0])
    
    # Tính toán số lượng pixel màu đen và màu trắng cho từng pixel trong các ma trận
    for binary in binaries:
        black_pixels += binary == 0
        white_pixels += binary == 255

    # So sánh số lượng pixel màu đen và màu trắng để quyết định màu sắc cuối cùng của pixel trong ma trận đặc trưng
    feature = np.zeros_like(binaries[0], dtype=np.uint8)
    for i in range(feature.shape[0]):
        for j in range(feature.shape[1]):
            if black_pixels[i][j] > white_pixels[i][j]:
                feature[i][j] = 0
            else:
                feature[i][j] = 255

    return feature

features = []
folder_path = "E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/char/"
files = os.listdir(folder_path)
for file in files:
    if os.path.isdir(os.path.join(folder_path, file)):
        folder_path_ii = os.path.join(folder_path, file)
        features.append(feature(folder_path_ii, file))
        
features2 = []
folder_path = "E:/BKDN/Season_3_Term_2/PBL5/pbl5_app/PBL5-Car-Lisence-Plate-Recognition-Application-v2/My-App-PBL5/char2line/"
files = os.listdir(folder_path)
for file in files:
    if os.path.isdir(os.path.join(folder_path, file)):
        folder_path_ii = os.path.join(folder_path, file)
        features2.append(feature(folder_path_ii, file))
        
def predict(binary, number, features):
    n = 0
    max = 0
    i = 0

    # number == 1: kí tự đang đọc là kí tự chữ số
    if (number == 1):

        # Đọc từ 0 đến 9
        for i in range (10):
            # Tính số pixel giống nhau của chữ số cần dự đoán và đặc trưng của các chữ số
            matching_pixels = np.sum(binary == features[i])
            total_pixels = binary.shape[0] * binary.shape[1]

            # Tính % giống nhau bằng cách lấy số pixel giống nhau / tổng số pixel * 100
            matching_percentage = matching_pixels / total_pixels * 100

            # Lấy max = tỉ lệ khớp nhất của chữ số cần dự đoán với các chữ số đặc trưng, n là chữ số được dự đoán
            if (matching_percentage>max): 
                n = i
                max = matching_percentage

    # number == 0: kí tự đang đọc là kí tự chữ cái
    else:

        # Nếu không phải chữ số thì đọc các feature chữ cái
        for i in range(10, len(features)):
            matching_pixels = np.sum(binary == features[i])
            total_pixels = binary.shape[0] * binary.shape[1]
            matching_percentage = matching_pixels / total_pixels * 100
            if (matching_percentage>max): 
                n = i
                max = matching_percentage
    # print(n,max)
    if (n == 7 and max < 65): 
        n = 1
    # print(n, max)
    return n, max

def read_char(labels_list, max, type):
    sorted_list = sorted(labels_list, key=lambda x: x[0])
    if (len(labels_list) > max):
        delete = len(labels_list) - max
    else:
        delete = 0
    predicted = []
    if (type == 0):
        for i in range(len(sorted_list)):
            x, dg, y = sorted_list[i]
            predicted.append((i, predict(dg, 1, features), predict(dg, 0, features)))
    
    else:
        for i in range(len(sorted_list)):
            x, dg, y = sorted_list[i]
            predicted.append((i, predict(dg, 1, features2), predict(dg, 0, features2)))
    predicted = sorted(predicted, key=lambda x: x[1][1], reverse=True)
    predicted_string = ""
    j = 0
    lst = [list(item) for item in predicted]
    # print(lst)
    if (type == 0):
        for i in reversed(range(len(predicted))):
            if (j == delete):
                break
            if (lst[i][0] < 2):
                lst.remove(lst[i])
                j = j + 1
            elif (lst[i][0] > (2+ delete)):
                lst.remove(lst[i])
                j = j + 1
            else:
                if (lst[i][2][1] >= 65):
                    lst.remove(lst[i-1])
                    j = j + 1
                else:
                    lst.remove(lst[i])
                    j = j + 1
    if (type == 1):
        for i in reversed(range(len(predicted))):
            if (j == delete):
                break
            # print(lst[i])
            if (lst[i][0] < 2):
                lst.remove(lst[i])
                j = j + 1
            else:
                if (lst[i][2][1] >= 65):
                    # print(lst[i-1])
                    lst.remove(lst[i-1])
                    j = j + 1
                else:
                    # print(lst[i])
                    lst.remove(lst[i])
                    j = j + 1
    if (type == 2):
        if (delete != 0):
            for i in range (delete):
                lst.pop(-1)

    predicted = [tuple(item) for item in lst] # chuyển lại thành tuple
    i = 0
    # print(predicted)
    for item in sorted(lst, key=lambda x: x[0]):
            i = i + 1
            # print(item)
            if (i == 3 and type == 0):
                if (item[2][0] == 10):
                    predicted_string += "A"
                if (item[2][0] == 11):
                    predicted_string += "B"
                if (item[2][0] == 12):
                    predicted_string += "C"
                if (item[2][0] == 13):
                    predicted_string += "D"
                if (item[2][0] == 14):
                    predicted_string += "F"
                if (item[2][0] == 15):
                    predicted_string += "G"
                if (item[2][0] == 16):
                    predicted_string += "L"
                if (item[2][0] == 17):
                    predicted_string += "N"
                if (item[2][0] == 18):
                    predicted_string += "S"
                if (item[2][0] == 19):
                    predicted_string += "V"
                if (item[2][0] == 20):
                    predicted_string += "Y"
                if (item[2][0] == 21):
                    predicted_string += "Z"
            elif (i==3 and type == 1):
                if (item[2][0] == 10):
                    predicted_string += "A"
                if (item[2][0] == 11):
                    predicted_string += "E"
                if (item[2][0] == 12):
                    predicted_string += "G"
            else:
                predicted_string += str(item[1][0])
    # print(predicted_string)
    return predicted_string

def read(cropped_image, type):
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    # Sử dụng hàm connectedComponents để tìm các vùng kết nối trên ảnh nhị phân
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    num_labels, labels = cv2.connectedComponents(binary)

    d = 0
        # Sử dụng hàm connectedComponentsWithStats để tính toán diện tích của các vùng kết nối
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)
    for i in range(num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area < 90 or area > 1500:
            labels[labels == i] = 0
        else: 
            d = d+1
    
    x_centroids = centroids[:, 0]
    y_centroids = centroids[:, 1]
    
    labels_list = []

    if (d > 5):
        # print(d)
        for i in range(1, num_labels):
            # Lấy thông tin của nhãn hiện tại
            x, y, w, h, area = stats[i]

            # Nếu diện tích của nhãn nằm trong khoảng từ 100 đến 1500
            if 90 < area < 1500:
                # Cắt ảnh của nhãn hiện tại từ ảnh gốc
                digit_img = binary[y:y+h, x:x+w]
                digit_img = cv2.resize(digit_img, (25,60))
                # print(x_centroids[i], y_centroids[i])
                labels_list.append((x_centroids[i], digit_img, y_centroids[i]))   
                # print(labels_list)      
    else:
        return ""
    
    read_final = None
    if (type == 1):
        max = 8
        read_final = read_char(labels_list, max, 0)
        # print(s)
    else: 
        label_distances = []
        first_label = min(labels_list, key=lambda label: label[0])
        first_x_centroid, first_digit_img, first_y_centroid = first_label
        predicted = predict(first_digit_img, 1,  features2)
        while (len(labels_list) > 8):
            if (predicted[1] < 65):
                for i, label in enumerate(labels_list):
                    if label == first_label:
                        del labels_list[i]
                        break
                first_label = min(labels_list, key=lambda label: label[0])
                first_x_centroid, first_digit_img, first_y_centroid = first_label
                predicted = predict(first_digit_img, 1, features2)
            else:
                break
            
        line1 = []
        line2 = []
        i = 0
        labels_list.sort(key=lambda x: x[0])
        # print(labels_list)
        for label in labels_list:
            x_centroid, digit_img, y_centroid = label
            distance = abs(y_centroid - first_y_centroid)
            distance_x = abs(x_centroid - first_x_centroid)
            label_distances.append(distance)
            if (distance >= 6 + i*1.5):
                line1.append(label)  
            else:
                line2.append(label)
            i = i + 1

        # print(len(line1), len(line2))
        # print(label_distances)
        max_line1 = 3
        max_line2 = 5
        line1 = read_char(line1, max_line1, 1)
        line2 = read_char(line2, max_line2, 2)
        read_final = line1 + line2
        # print(read_final)

    return read_final


def readPlate(image, model):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model(image)

    for i, det in enumerate(results.xyxy[0]):
        type = 0
        # Lấy tọa độ bbox của vật thể thứ i
        bbox = det[0:4].cpu().numpy()

        # Cắt lấy vùng ảnh nằm trong bbox
        cropped_image = image[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
        # Chuyển mảng numpy thành mảng 2 chiều
        cropped_image_2d = np.squeeze(np.asarray(cropped_image))

        max_value = np.amax(cropped_image_2d)
        # Tính tỉ lệ chiều dài/ chiều rộng của biển số
        ratio = (bbox[2]-bbox[0])/(bbox[3]-bbox[1])
        if (ratio >= 2.2):
            type = 1
            cropped_image = cv2.resize(cropped_image, (256, 100))
        else:
            type = 2
            cropped_image = cv2.resize(cropped_image, (550, 100))
        
        # print("Type: ", type)
        read_fn = read(cropped_image, type)
        # print(read_fn)
        return type, read_fn, max_value, cropped_image
    
# # Tạo một đối tượng VideoCapture để đọc video
# cap = cv2.VideoCapture(0)

# # Lấy kích thước khung hình của video
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# # Đọc từng khung hình của video, xử lý và ghi lại
# result_s = ''
# r = 0

# with open("license_plates_history.txt", "w") as file:
#     file.write('')

# max_value_before = 0
# id = 1
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     #Xử lý khung hình ở đây
#     processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = model(processed_frame)
    
#     if len(results.pred[0]) >= 1:
#         if (results.pred[0][0][3] >= height*4/5 and r == 1):
#             #arduino.sendData([0])
#             r = 0
#         for i in range (len(results.pred[0])):
#             accuracy = float(results.pred[0][i][4].item())
#             # print(results.pred)
#             if (accuracy >= 0.7 and (results.pred[0][i][2].item() - results.pred[0][i][0].item()) >= 120 and r == 0 and results.pred[0][i][3] < height*4/5):
#                 if (readPlate(processed_frame,model) != None):
#                     k, result_s, max_value, cropped_image = readPlate(processed_frame,model)
#                     if (max_value < 255):
#                         if (max_value >= max_value_before):
#                             result_before = result_s
#                             result_s = ""
#                             max_value_before = max_value
#                         else:
#                             result_s = result_before
#                             print(max_value_before)
#                 if (result_s != ""):
#                     r = 1
#                     #arduino.sendData([1])
#                     cv2.imwrite(f"{id}.jpg", cropped_image)
#                     with open('license_plates_history.txt', 'a') as file:
#                         file.write('{} {}\n'.format(id, result_s))
#                         id = id + 1
#     else:
#         r = 0
#         #arduino.sendData([0])

#     #Vẽ chuỗi result_s lên khung hình results
#     cv2.putText(results.render()[0], result_s, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
#     if (r == 0):
#         cv2.putText(results.render()[0], "Next license plate!", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
#     # # Hiển thị khung hình đã xử lý
#     cv2.imshow('Processed Frame', cv2.cvtColor(results.render()[0], cv2.COLOR_RGB2BGR))
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Giải phóng các tài nguyên và đóng các cửa sổ hiển thị
# cv2.destroyAllWindows()
