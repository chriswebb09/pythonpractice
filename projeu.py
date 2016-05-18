import math

def fact(n):
	if not n:
		return 1
	else:
		return n * fact(n -1)


def pidigits():
    pig = str(math.pi)
    for i in xrange(12):
        print pig[i]

pidigits()
"""
def get_div_numbers():
	x = 1
	y = []
	while x < 1000:
		if x % 3 == 0 or x % 5 == 0:
			y.append(x)
		x += 1
	return sum(y)
"""
"""
def palindrom():
	x = 100
	pal_list = []
	check_num = str(x)
	if check_num == check_num[::-1]:
		print check_num
		x += 1
	pal_list.sort()
	print pal_list

palindrom()
"""




