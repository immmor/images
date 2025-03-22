# 图片路径
# image_path = '1341742455832_.pic.jpg'
# image_path = '1321742455732_.pic.jpg'
# image_path = '41742358957_.pic.jpg'
# image_path = '31742358953_.pic.jpg'
image_path = '651742440485_.pic.jpg'

from paddleocr import PaddleOCR

# 创建 PaddleOCR 实例，使用中文识别模型
# 计算程序运行时间
import time

start_time = time.time()
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

def paddle_ocr_chinese(image_path):
    try:
        # 进行 OCR 识别
        result = ocr.ocr(image_path, cls=True)
        # 提取识别到的文本
        texts = []
        for line in result[0]:
            texts.append(line[1][0])
        # 将文本拼接成一个字符串
        full_text = '\n'.join(texts)
        return full_text
    except Exception as e:
        print(f"发生错误: {e}")
        return None

if __name__ == "__main__":
    # 替换为你的图像文件路径
    # image_path = 'your_image.jpg'
    result = paddle_ocr_chinese(image_path)
    # from ollama import ChatResponse, chat
    # prompt = "提取下面的内容并用json格式输出。需要展示包括检查部位之前的信息。也需要提取超声所见、超声印象（或者超声提示）的信息。超声所见的内容包括超声所见和超声印象（或者超声提示）之间的所有内容，不要把里面的东西拆开。直接显示键，不要翻译，不要说英文。\n" + result
    # response: ChatResponse = chat(model='qwen2.5:latest', messages=[
    #     {
    #         'role': 'user',
    #         'content': prompt,
    #     },
    # ])
    # bot_response = response.message.content
    if result:
        print("识别结果:")
        print(result)
        # print("json:")
        # print(bot_response)
    print(f"程序运行时间: {time.time() - start_time} 秒")
