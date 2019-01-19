print('我们来玩猜数字游戏吧,来开始啦.')
a = int(input('请输入一个数字:'))
if a >= 10:
    print('你猜的数字好大啊.')
elif 2 <= a <10:
	print('猜到啦')
else:
    print('你猜的数字好小啊')