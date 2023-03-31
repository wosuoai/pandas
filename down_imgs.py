import pandas as pd
import requests

def read_file(filePath: str, fileName: str, fileType: str):
    # 所有文件跳过第一行
    if fileType == "excel":
        df = pd.read_excel(filePath + "/" + fileName, skiprows=1)
    if fileType == "csv":
        df = pd.read_csv(filePath + "/" + fileName, skiprows=1)
    return df


def main(filePath: str, fileName: str, fileType: str):
    df = read_file(filePath, fileName, fileType)
    # 把每行数据都变成列表
    allIndexList = df.values.tolist()
    count=0

    for indexList in allIndexList:
        for value in indexList:
            count += 1
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
            r = requests.get(value, headers=headers)
            # 下载图片
            with open("images/{}.jpg".format(count), mode="wb") as f:
                f.write(r.content)  # 图片内容写入文件


if __name__ == "__main__":
    main(r"C:\Users\admin\PycharmProjects\crawl", "图片链接.xlsx", "excel")
