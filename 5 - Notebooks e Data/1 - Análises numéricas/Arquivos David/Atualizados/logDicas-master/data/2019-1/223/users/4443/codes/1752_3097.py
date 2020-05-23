p = int(input("Digite a posicao de chegada do joquei: "))

c = 0
soma = 0
while (p != 0):
	if (p == 1):
		soma = soma + 25
	elif (p == 2):
		soma = soma + 18
	elif (p == 3):
		soma = soma + 12 
	elif (4 <= p <= 10):
		soma = soma + (14 - p)
	c = c + 1
	p = int(input("Digite a posicao de chegada do joquei: "))
print(soma)	