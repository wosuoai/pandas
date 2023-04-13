import os
import pandas as pd

# 需要合并的excel文件夹
input_folder = 'C:\\Users\\admin\\PycharmProjects\\义乌购\\test'

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
    combined_df = pd.concat(all_data_frames, axis=0, ignore_index=True) #带搜索处理的文件总表
    print("合并后的表格共计%s行数据" %combined_df.shape[0])
else:
    print('未找到文件')

#筛选符合条件的数据
combined_df = combined_df[combined_df['访客数(UV)']>=50]
#删除完全重复的行
combined_df.drop_duplicates()
#对"来源"列进行去重，对于重复项，保留第一次出现的值
combined_df.drop_duplicates('来源', keep='first')
df = pd.DataFrame(combined_df["来源"])
df.to_excel('./{}.xlsx'.format('访问来源总表'))
