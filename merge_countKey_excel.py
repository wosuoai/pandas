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
    print(combined_df.shape)
else:
    print('未找到文件')


#search_data = pd.read_excel("C:\\Users\\admin\\PycharmProjects\\义乌购\\义乌购商品列表\\商品列表总表.xlsx",sheet_name="Sheet1")
# 关键词数据信息
key_data = pd.read_excel("C:\\Users\\admin\\PycharmProjects\\义乌购\\义乌购近30天访问来源\\访问来源总表次数.xlsx",sheet_name="Sheet1")

keywordList = []
appear_numList = []
for key in key_data["关键词"]:
    tmp_df = combined_df[(combined_df['标题'].str.find(key) != -1)]
    keywordList.append(key)
    appear_numList.append(tmp_df.shape[0])

df = pd.DataFrame({"关键词":keywordList,"出现次数":appear_numList})
df.to_excel('./{}.xlsx'.format('商品列表总表关键词出现次数统计'))
