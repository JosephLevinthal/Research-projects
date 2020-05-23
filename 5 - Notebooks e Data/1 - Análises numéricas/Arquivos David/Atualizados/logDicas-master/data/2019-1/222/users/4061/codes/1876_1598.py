from numpy import*
valor = array(eval(input("digite valor: ")))
soma = 0
cont = 0
desc = 5.00

while(valor > 80.00 and valor < 80.00):
	if(valor > 80.00):
		valor = valor - desc
		cont = cont + 1
		soma = soma + 1
	else:
		cont = cont + 1
		soma = soma + 1
print(round(valor, 2))

