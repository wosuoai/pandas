import pandas as pd

data = pd.read_excel("C:\\Users\\admin\\PycharmProjects\\义乌购\\义乌购近30天访问来源\\Y4005303.xls",sheet_name="Sheet1")
data = data[data['访客数(UV)']>=50]
df = pd.DataFrame(data)
df.to_excel('./{}.xlsx'.format('访问来源总表'))
