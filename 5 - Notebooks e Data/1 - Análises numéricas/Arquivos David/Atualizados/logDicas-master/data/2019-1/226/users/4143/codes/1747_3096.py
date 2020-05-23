: 
a = int(input("Posicao de chegada:"))
soma = 0
while (a!=0):
	if (a ==1):
		a = 20
		soma = soma + a
	elif (a==2):
		a = 15
		soma = soma +a
	elif (a==3):
		a = 10
		soma = soma+a
	elif (4<= a <=11):
		a = 11 - a
		soma = soma + a
	a = int(input("Posicao:"))
print(soma)