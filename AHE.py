import cv2
import numpy as np
from matplotlib import pyplot as plt
import image_slicer
from image_slicer import join
from PIL import Image
abc = cv2.imread("IMG_0116.jpg")
# Gọi ảnh    
img = 'IMG_0116.jpg'
num_tiles = 25
# Cắt ảnh thành 25 phần bằng nhau
tiles = image_slicer.slice(img, num_tiles)

# Thực hiện cân bằng cho từng ảnh nhỏ
for tile in tiles:
    #Thực hiện đọc ảnh trong tệp hình ảnh và lưu trữ trong 1 đối tượng
    img = cv2.imread(tile.filename)
    # Thực hiện cân bằng histogram
    b,g,r = cv2.split(img)
    # Cân bằng biểu đồ bằng cách sử dụng hàm equalizeHist
    equ_b = cv2.equalizeHist(b)
    equ_g = cv2.equalizeHist(g)
    equ_r = cv2.equalizeHist(r)
    #Gộp 3 kênh thành 1 chuỗi cuối sau khi cân bằng
    equ = cv2.merge((equ_b, equ_g, equ_r))
    cv2.imwrite(tile.filename,equ)
    # Thực hiện việc cập nhật dữ liệu cho đối tượng hình ảnh của từng ô bằng việc mở lại hình ảnh trong ô bất cứ khi nào tệp tin thay đổi
    tile.image = Image.open(tile.filename)
# Thực hiện việc nối các chuỗi ảnh nằm trong tiles để tạo ra ảnh cuối
image = join(tiles)
# Tạo GUI hiển thị
f, axes = plt.subplots(2,2, figsize=(30,20))
axes[0, 0].imshow(abc)
axes[0, 0].set_title('input')
axes[0, 1].imshow(image)
axes[0, 1].set_title('AHE')
plt.show()
plt.close()
image.save("Output_AHE.jpg")