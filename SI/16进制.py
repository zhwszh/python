def sjz(i):
    if i <= 9:
        return i
    elif 10 <= i <= 15:
        a = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
        b = a[i]
        return b
    else i >= 15:



n = int(input("输入一个十进制数:"))
print('十六进制数为:',sjz(n))
