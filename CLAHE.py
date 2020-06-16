# Cân bằng CLAHE cho ảnh màu và xám
"""
Chuyển hình ảnh sang lab color. Vì lab color có 3 kênh là
L : biểu diễn độ sáng
a : chứa các giá trị màu Green -> Red 
b : chứa các giá trị màu Blue -> Yellow
Chúng ta chỉ thực hiện cân bằng CLAHE trên kênh L để tăng giảm độ tương phản
không làm ảnh hưởng tới màu sắc của ảnh
"""
import numpy as np
import cv2 
from matplotlib import pyplot as plt
def CLAHE(image):


    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Chia ảnh trên thành 3 kênh màu L,a,b
    l, a, b = cv2.split(lab)

    # Thực hiện cân bằng CLAHE trên kênh L
    # Ngưỡng giới hạn độ tương phản = 3
    # đặt kích thước của lưới là 8x8 để cân bằng
    clahe = cv2.createCLAHE( tileGridSize=(2, 2))
    # Áp dụng cho kênh L
    cl = clahe.apply(l)

    # Hợp nhất 3 kênh lại với nhau tạo thành hình ảnh lab color
    limg = cv2.merge((cl, a, b))

    # Chuyển hình ảnh từ màu lab color sang màu RGB và xuất ra màn hình
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    # Tạo GUI xuất ảnh và biểu đồ
    f, axes = plt.subplots(2,2, figsize=(30,20))
    axes[0, 0].imshow(image)
    axes[0, 0].set_title('input')
    axes[0, 1].imshow(final)
    axes[0, 1].set_title('CLAHE')
    axes[1, 0].hist(bgr.flatten(), 256, [0,256])
    axes[1, 1].hist(lab.flatten(), 256, [0,256])
    plt.show()
    plt.close()
    # Lưu ảnh
    cv2.imwrite('output_name_CLAHE.png', final)
bgr = cv2.imread('car.jpg')
CLAHE(bgr)

