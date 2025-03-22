import cv2
import pytesseract
import pandas as pd

# 加载图像
image = cv2.imread('651742440485_.pic.jpg')

# 图像预处理（提取表格线）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
edges = cv2.Canny(binary, 50, 150)

# 使用Tesseract提取文本
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(binary, config=custom_config)

# 将文本整理为表格数据
rows = text.split('\n')
data = [row.split() for row in rows]
df = pd.DataFrame(data)

# 打印表格数据
print(df)
