import os
import pandas as pd


input_folder = 'C:\\Users\\admin\\PycharmProjects\\test'
output_file = 'C:\\Users\\admin\\PycharmProjects\\test1\\file.xlsx'

#  获取文件夹下所有的Excel文件
excel_files = [file for file in os.listdir(input_folder) if file.endswith('.xls')]

#  如果存在Excel文件，则整合为一个新的Excel文件
if excel_files:
    #  创建DataFrame列表，用于保留所有Excel文件中的数据
    all_data_frames = []

    #  遍历Excel文件，并将它们读入DataFrame列表中
    for file in excel_files:
        file_path = os.path.join(input_folder, file)
        data_frame = pd.read_excel(file_path)
        all_data_frames.append(data_frame)

    #  将所有数据合并到一个DataFrame中，并将它写入输出文件中
    combined_df = pd.concat(all_data_frames, axis=0, ignore_index=True)
    combined_df.to_excel(output_file, index=False)
else:
    print('未找到文件')
