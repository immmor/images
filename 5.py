import cv2
import numpy as np
from PIL import Image

# 读取图片
img = Image.open('651742440485_.pic.jpg').convert('RGB')  # 确保图像模式为RGB

# 转换为灰度图像
gray_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

# 二值化
_, binary_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY_INV)  # 可能需要调整阈值

# 检测轮廓
contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 分割表格
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    cropped_img = img.crop((x, y, x + w, y + h))

    # 将cropped_img转换为RGB模式以防其原始模式是RGBA
    if cropped_img.mode in ('RGBA', 'LA') or (cropped_img.mode == 'P' and 'transparency' in cropped_img.info):
        alpha = cropped_img.convert('RGBA').split()[-1]
        bg_colour = (255, 255, 255)  # 白色背景
        cropped_img = cropped_img.convert('RGBA')
        bg = Image.new('RGBA', cropped_img.size, bg_colour + (255,))
        bg.paste(cropped_img, mask=alpha)
        cropped_img = bg.convert('RGB')

    cropped_img.save(f'cropped_{i}.jpg')

print("分割完成！")
