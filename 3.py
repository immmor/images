import easyocr

# 初始化EasyOCR
reader = easyocr.Reader(['ch_sim', 'en'])  # 支持中文和英文

# 从图像中提取文本
result = reader.readtext('651742440485_.pic.jpg')

# 打印识别结果
for detection in result:
    print(detection[1])  # detection[1] 是识别出的文本
