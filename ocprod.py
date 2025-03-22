from flask import Flask, request, jsonify
from paddleocr import PaddleOCR
import time, json
from ollama import ChatResponse, chat

app = Flask(__name__)

# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

def paddle_ocr_chinese(image_path):
    try:
        result = ocr.ocr(image_path, cls=True)
        texts = []
        for line in result[0]:
            texts.append(line[1][0])
        full_text = '\n'.join(texts)
        return full_text
    except Exception as e:
        print(f"发生错误: {e}")
        return None

def remove_content(s):
    first_brace_index = s.find('{')
    last_brace_index = s.rfind('}')
    if first_brace_index == -1 or last_brace_index == -1:
        return ""
    result = s[first_brace_index:last_brace_index + 1]
    return result

@app.route('/ocr', methods=['POST'])
def ocr_api():
    data = request.json
    image_path = data.get('image_path')
    if not image_path:
        return jsonify({'error': '未提供图片路径'}), 400

    start_time = time.time()
    result = paddle_ocr_chinese(image_path)
    if result is None:
        return jsonify({'error': 'OCR 识别失败'}), 500

    prompt = "提取下面的内容并用json格式输出。\n" + result
    response: ChatResponse = chat(model='qwen2.5:latest', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    bot_response = response.message.content

    json_content = remove_content(bot_response)
    try:
        json_data = json.loads(json_content)
    except json.JSONDecodeError as e:
        return jsonify({'error': '提取的内容不是一个有效的 JSON 格式'}), 500

    print(f"程序运行时间: {time.time() - start_time} 秒")
    return jsonify(json_data), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
