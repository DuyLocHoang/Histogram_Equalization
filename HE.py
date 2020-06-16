import numpy as np
import cv2
from matplotlib import pyplot as plt

def argorithm_HE(img) : 
    # Tách ảnh thành 3 màu   
    b,g,r = cv2.split(img)
    # đếm số lần xuất hiện của các pixels và lấy bản sao trải ra thành mảng 1 chiều
    h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256]) # Mỗi pixel được biểu diễn 0-255 giá trị
    h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
    h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
    # Tính toán hàm tích luỹ cho từng mức xám   
    cdf_b = np.cumsum(h_b)  
    cdf_g = np.cumsum(h_g)
    cdf_r = np.cumsum(h_r)
    # Chương trình thực hiện việc cân bằng mức xám
    # Cân bằng cho màu blue
    cdf_m_b = np.ma.masked_equal(cdf_b,0)   #Tạo mặt nạ tất cả các giá trị trong mảng
    
    cdf_m_b = (cdf_m_b)*255/(cdf_m_b.max()) #Tính toán các giá trị theo công thức histogram equalization phần lý thuyết
      
    cdf_final_b = np.ma.filled(cdf_m_b,0).astype('uint8')   #Điền vào các giá trị vừa tính được  và ép kiểu int vào các dữ liệu bị che
    # Cân bằng cho màu green
    cdf_m_g = np.ma.masked_equal(cdf_g,0)
    cdf_m_g = (cdf_m_g)*255/(cdf_m_g.max())
    cdf_final_g = np.ma.filled(cdf_m_g,0).astype('uint8')
    # Cân bằng cho màu red
    cdf_m_r = np.ma.masked_equal(cdf_r,0)
    cdf_m_r = (cdf_m_r)*255/(cdf_m_r.max())
    cdf_final_r = np.ma.filled(cdf_m_r,0).astype('uint8')

    # hợp nhất các mảng thành trong ba kênh tạo ra ảnh cuối
    img_b = cdf_final_b[b]
    img_g = cdf_final_g[g]
    img_r = cdf_final_r[r]
    img_out = cv2.merge((img_b, img_g, img_r))

    #Lưu file ảnh vừa cân bằng và hiển thị ra GUI
    cv2.imwrite('output_name.png', img_out)
    f, axes = plt.subplots(2,2, figsize=(30,20))
    axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('input')
    axes[0, 1].imshow(cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB))
    axes[0, 1].set_title('HE')
    axes[1, 0].hist(b.flatten(), 256, [0,256], color ='b')
    axes[1, 0].hist(g.flatten(), 256, [0,256], color ='g')
    axes[1, 0].hist(r.flatten(), 256, [0,256], color ='r')
    axes[1, 1].hist(img_b.flatten(), 256, [0,256], color = 'b')
    axes[1, 1].hist(img_g.flatten(), 256, [0,256], color ='g')
    axes[1, 1].hist(img_r.flatten(), 256, [0,256], color = 'r')
    plt.show()
    plt.close()
    
def HE(img) :
    # Phân tách thành 3 kênh màu
    b,g,r = cv2.split(img)
    # Cân bằng biểu đồ bằng cách sử dụng hàm equalizeHist
    equ_b = cv2.equalizeHist(b)
    equ_g = cv2.equalizeHist(g)
    equ_r = cv2.equalizeHist(r)
    #Gộp 3 kênh thành 1 biểu cuối sau khi cân bằng
    equ = cv2.merge((equ_b, equ_g, equ_r))
    cv2.imwrite('output_name_HE.png', equ)
    f, axes = plt.subplots(2,2, figsize=(30,20))
    axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('input')
    axes[0, 1].imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
    axes[0, 1].set_title('HE')
    axes[1, 0].hist(b.flatten(), 256, [0,256], color ='b')
    axes[1, 0].hist(g.flatten(), 256, [0,256], color ='g')
    axes[1, 0].hist(r.flatten(), 256, [0,256], color ='r')
    axes[1, 1].hist(equ_b.flatten(), 256, [0,256], color = 'b')
    axes[1, 1].hist(equ_g.flatten(), 256, [0,256], color ='g')
    axes[1, 1].hist(equ_r.flatten(), 256, [0,256], color = 'r')
    
    plt.show()
    plt.close()

bgr = cv2.imread('night.png')

argorithm_HE(bgr)
