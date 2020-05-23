p = int(input("posicao de chegada: "))

i = 0
soma = 0
while(p !=0):
	if(p == 1):
		soma = soma + 25
		i = i + 1
		p = int(input("posicao: "))
	elif(p == 2):
		soma = soma + 18
		i = i + 1
		p = int(input("posicao: "))
	elif(p == 3):
		soma = soma + 12
		i = i + 1
		p = int(input("posicao: "))
	elif(p >= 4 and p <= 10):
		soma = soma + (14 - p)
		i = i + 1
		p = int(input("posicao: "))
	else:
		soma = soma
		p = int(input("posicao: "))

print(soma)