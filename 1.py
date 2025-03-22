from paddleocr import PaddleOCR, draw_ocr
import cv2
import numpy as np

# 初始化PaddleOCR，use_gpu可以设置为True使用GPU加速
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # 中文模型，如果需要其他语言可以修改

# 读取图片
img_path = '651742440485_.pic.jpg'
img = cv2.imread(img_path)

# 进行OCR检测和识别
result = ocr.ocr(img_path, cls=True)

# 结果处理
boxes = [line[0] for line in result]  # 检测框
txts = [line[1][0] for line in result]  # 识别的文本
scores = [line[1][1] for line in result]  # 识别的置信度

# 绘制检测结果
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
im_show = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
im_show = cv2.cvtColor(np.array(im_show), cv2.COLOR_RGB2BGR)

# 显示结果
cv2.imwrite('result.jpg', im_show)
cv2.imshow('result', im_show)
cv2.waitKey(0)
