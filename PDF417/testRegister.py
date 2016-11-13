import register

dataDict = register.main('bar.jpeg')

for data in dataDict:
    print(data, ':', dataDict[data])
