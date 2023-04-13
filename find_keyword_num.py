import pandas as pd

search_data = pd.read_excel("C:\\Users\\admin\\PycharmProjects\\义乌购\\义乌购商品列表\\商品列表总表.xlsx",sheet_name="Sheet1")
key_data = pd.read_excel("C:\\Users\\admin\\PycharmProjects\\义乌购\\义乌购近30天访问来源\\访问来源总表次数.xlsx",sheet_name="Sheet1")

keywordList = []
appear_numList = []
for key in key_data["关键词"]:
    tmp_df = search_data[(search_data['标题'].str.find(key) != -1)]
    keywordList.append(key)
    appear_numList.append(tmp_df.shape[0])

df = pd.DataFrame({"关键词":keywordList,"出现次数":appear_numList})
df.to_excel('./{}.xlsx'.format('商品列表总表关键词出现次数统计'))
