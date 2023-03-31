import pandas as pd


def read_file(filePath: str, fileName: str, fileType: str):
    # 所有文件跳过第一行
    if fileType == "excel":
        df = pd.read_excel(filePath + "/" + fileName, skiprows=1)
    if fileType == "csv":
        df = pd.read_csv(filePath + "/" + fileName, skiprows=1)
    return df


def main(filePath: str, fileName: str, fileType: str):
    # 存放统计结果的列表
    countItemDict = {}
    # 存放原始数据的列表
    valueList = []
    df = read_file(filePath, fileName, fileType)
    print(df)
    # 把每行数据都变成列表
    allIndexList = df.values.tolist()

    # 遍历所有行数据去重
    for indexList in allIndexList:
        for value in indexList:
            # 跳过pandas的空值
            if pd.isnull(value):
                continue
            valueList.append(value)

    # 通过集合实现类别
    itemNameList = list(set(valueList))
    # print(len(itemNameList))
    # print(itemNameList)

    # 默认先建立练习赋值为0
    for itemName in itemNameList:
        countItemDict[itemName] = 0

    # 统计key不同数量
    for key in valueList:
        countItemDict[key] = countItemDict[key] + 1
    # print(countItemDict)
    # print(len(countItemDict))

    countNameList = [i for i in countItemDict.keys()]
    countNameValueList = [i for i in countItemDict.values()]
    # print(countNameList)
    ## 存入统计结果
    data = {'类型': countNameList,
            '类型数量': countNameValueList}
    write_pd = pd.DataFrame(data)
    write_pd.to_excel("%scount.xlsx" % (fileName.split(".")[0]))


if __name__ == "__main__":
    main(r"C:\Users\admin\PycharmProjects\crawl", "图片链接.xlsx", "excel")
    # get_file_value()
    # print(read_file(r"C:\Users\15256\Desktop\dealFile","袜子批发.xlsx","excel"))
