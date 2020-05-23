n = int(input(" "))

cont = 0

for i in range(n,0,-1):
	print(i*'*' + 'o'*cont + i*'*')
	cont = cont + 2