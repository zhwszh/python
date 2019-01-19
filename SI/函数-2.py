
def bhg(list):

    a = []
    for i in list:
        if i < 20:
            a.append(i)
            c = len(a)
    return c

list = [22, 23, 20, 19, 21, 22, 22, 23, 24, 20, 20, 22]
xx = bhg(list)

print('一年有%d次考勤不合格.' % xx)

