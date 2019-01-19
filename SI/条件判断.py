data = [21, 22, 22, 20, 23, 19, 20, 21, 23, 20, 22, 20]
data_1=[]
for i in data:
    if i < 20:
        data_1.append(i)
        print(data_1)
if data_1:
        print("考勤不合格")
