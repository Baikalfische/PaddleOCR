def replace_prefix(input_file):
    # 读取文件内容
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 重新写回同一个文件，并将 'image_train/' 替换为空
    with open(input_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            # 将 'image_train/' 替换为空，只留下数字部分
            line = line.replace('image_test/', '')
            outfile.write(line)

# 替换成你的文件路径
input_file = "C:/FAU/OCR/PP-OCR/PaddleOCR/train_data/trainval.txt"

replace_prefix(input_file)


