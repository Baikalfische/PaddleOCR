def replace_prefix(input_file):
    # 读取文件内容
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 重新写回同一个文件，并将 'test_data' 替换为 'images'
    with open(input_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            # 将 'test_data' 替换为 'images'
            line = line.replace('images', 'images/dicdelta')
            outfile.write(line)

# 替换成你的文件路径
input_file = 'C:/FAU/OCR/数据集/dicdelta(rec)/dicdelta/val.txt'

replace_prefix(input_file)


