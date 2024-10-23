def cut_labels(input_file, output_file, keyword):
    # 打开输入文件并读取所有行
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 找到第一个包含关键字的行号
    cut_index = None
    for index, line in enumerate(lines):
        if keyword in line:
            cut_index = index
            break

    # 如果找到了关键字
    if cut_index is not None:
        # 保存从 cut_index 开始的所有行到新的文件
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(lines[cut_index:])
        
        # 更新原始文件，保留关键字之前的内容
        with open(input_file, 'w', encoding='utf-8') as infile:
            infile.writelines(lines[:cut_index])

    else:
        print(f"没有找到包含关键字 '{keyword}' 的行。")

# 文件路径和关键字
input_file = 'C:/FAU/OCR/数据集/dataset(dec)/dataset/label.txt'   # 输入的文本文件路径
output_file = 'C:/FAU/OCR/数据集/dataset(dec)/dataset/test.txt'  # 输出保存的文本文件路径
keyword = 'image_750'  # 关键字

# 调用函数
cut_labels(input_file, output_file, keyword)
