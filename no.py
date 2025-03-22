import cv2
from paddleocr import PPStructure, draw_structure_result, save_structure_res

# 初始化 PPStructure 模型
table_engine = PPStructure(show_log=True)

# 读取图像
img_path = '651742440485_.pic.jpg'
img = cv2.imread(img_path)

# 进行表格识别
result = table_engine(img)

# 保存结果
# save_folder = './output'
# save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

# 打印结果
for line in result:
    line.pop('img')  # 移除图像数据，便于打印
    print(line)
