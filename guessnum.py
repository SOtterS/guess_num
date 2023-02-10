import random
r = random.randint(1, 100)

while True:
	number = input('1-100猜一個數字： ')
	number = int(number)
	if r == number:
	    print('終於猜對了！')
	    break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')

