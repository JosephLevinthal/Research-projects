n = int(input('N: '))
a = '*'
o = 'o'
b = '*'

for i in range(n):
	f = a*(n-i)+(o*(i*2))+a*(n-i)
	print(f)