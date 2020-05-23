



n=int(input('digite n: '))
for linha in range(n):
	for j in range(n- linha):
		  print("*",end='')
	print('')

for linha in range(n):
	for j in range(linha+1):
		  print("*",end='')
	print('')
