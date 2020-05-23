n = int(input('N: '))
e = '*'

for i in range(n):
	f1 = e*(n-i)
	print(f1)
	
for i in range(n):
	f2 = e*(n-(n-i)+1)
	print(f2)