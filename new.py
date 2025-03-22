from paddleocr import PaddleOCR
import cv2

# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

def recognize_in_regions(image_path, regions):
    # 读取图片
    image = cv2.imread(image_path)
    results = []
    for region in regions:
        # 提取区域
        x, y, w, h = region
        cropped_image = image[y:y + h, x:x + w]
        # 对该区域进行 OCR 识别
        result = ocr.ocr(cropped_image, cls=True)
        results.append(result)
        # 在原图上绘制区域框
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 在区域上方显示识别结果
        text = " ".join([line[1][0] for line in result[0]])
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 显示结果图片
    cv2.imshow('OCR Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return results

# 示例：定义图片中的区域（x, y, width, height）
image_path = '651742440485_.pic.jpg'
regions = [
    (100, 100, 200, 200),
    (400, 100, 200, 200)
]

# 调用函数进行分区分框识别
ocr_results = recognize_in_regions(image_path, regions)
for i, result in enumerate(ocr_results):
    print(f"区域 {i + 1} 的识别结果:")
    for line in result[0]:
        print(line[1][0], f"置信度: {line[1][1]:.2f}")
