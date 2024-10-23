import re

def remove_duplicate_image_prefix(input_file, output_file):
    # 打开并读取输入文件
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # 找到并删除重复的 image_ 前缀，只保留后面的正确 image_x.jpg
    # 正则表达式匹配重复的 image_，并删除前一个
    cleaned_content = re.sub(r'(image_)\n\1', r'\1', content)

    # 写入到输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_content)

# 使用示例
input_file = 'C:/FAU/OCR/数据集/dataset(dec)/dataset/train.txt'  # 输入的文本文件路径
output_file = 'C:/FAU/OCR/数据集/dataset(dec)/dataset/train.txt'  # 输出格式化后的文件路径

remove_duplicate_image_prefix(input_file, output_file)


