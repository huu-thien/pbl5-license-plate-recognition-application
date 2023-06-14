import os

counter = 28  # Đặt giá trị ban đầu của counter là 28

for filename in os.listdir("."):  # Lặp qua tất cả các tệp trong thư mục hiện tại
    if filename.endswith(".txt"):  # Nếu tệp là tệp hình ảnh .jpg
        new_filename = "{}.txt".format(counter)  # Đặt tên mới cho tệp
        os.rename(filename, new_filename)  # Đổi tên tệp
        counter += 1  # Tăng giá trị của counter lên 1