from cnocr import CnOcr

# img_fp = './docs/examples/huochepiao.jpeg'
# image_path = '1341742455832_.pic.jpg'
# image_path = '1321742455732_.pic.jpg'
# image_path = '41742358957_.pic.jpg'
# image_path = '31742358953_.pic.jpg'
image_path = '651742440485_.pic.jpg'
ocr = CnOcr()  # 所有参数都使用默认值
out = ocr.ocr(image_path)

for item in out:
    print(item['text'])
