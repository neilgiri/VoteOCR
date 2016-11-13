import parserD

datas = parserD.main('sampleIN.txt')
for data in datas:
    print(data, ':', datas[data])
