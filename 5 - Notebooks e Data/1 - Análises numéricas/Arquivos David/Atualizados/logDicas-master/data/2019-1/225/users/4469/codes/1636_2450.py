a = input("Nome 1: ")
b = input("Nome 2: ")

contador = 0

if(a.upper()[contador] == b.upper()[contador]):
	while(a.upper()[contador] == b.upper()[contador]):
		contador = contador + 1
		
	if(a.upper()[contador] > b.upper()[contador]):
		print(b)
		print(a)
	else:
		print(a)
		print(b)
else:
	if(a.upper()[0] > b.upper()[0]):
		print(b)
		print(a)
	else:
		print(a)
		print(b)