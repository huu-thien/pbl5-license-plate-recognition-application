from PIL import Image
import os

# Lấy đường dẫn của folder hiện tại
current_dir = os.getcwd()

# Lặp qua tất cả các file trong folder hiện tại
for filename in os.listdir(current_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Chỉ xử lý file ảnh
        # Mở ảnh và resize nó
        img = Image.open(filename)
        img = img.resize((25, 60))
        
        # Lưu ảnh đã resize vào folder hiện tại
        img.save(filename)
