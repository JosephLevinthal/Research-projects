a = int(input())
while a >= 0:
	if a == 0:
		print('ARMSTROMG')
	else:
		j = 0
		for i in a:
			j += i**(len(a))
		if not(j == a):
			print('NAO ARMSTRONG')
		else:
			print('ARMSTRONG')
		a = int(input())