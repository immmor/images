import requests
import json

# 定义请求的URL
url = 'http://127.0.0.1:5000/ocr'

# 定义请求的JSON数据
data = {
    'image_path': '1321742455732_.pic.jpg'  # 替换为实际的图片路径
}

# 发送POST请求
response = requests.post(url, json=data)

# 打印响应内容
if response.status_code == 200:
    print("OCR识别成功:")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(response.text)
