
def juz(a):
    if 1 <= a <= 3:
        c = a * 6
        return c
    elif a > 3:
        c = a * 5
        return c
d = int(input('请输入需要购买的橘子重量/斤:'))
b = juz(d)
print('购买橘子总价为:'+ str(b))