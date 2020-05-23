n = int(input("Insira um numero natual diferente de 0:"))

cont = n

while(cont != 1):
	if(cont % 2 == 0):
		cont = cont // 2
		print(cont)
	else:
		cont = (cont*3) + 1
		print(cont)	