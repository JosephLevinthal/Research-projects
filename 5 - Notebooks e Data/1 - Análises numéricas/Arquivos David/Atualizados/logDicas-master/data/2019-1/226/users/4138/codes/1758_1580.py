from numpy import *
x = array(eval(input("insira as notas:")))
y = array(eval(input("nomes:")))

i = 0
soma = 0 # soma dos que faltaram
soma1 = 0 # soma dos aprovados
soma2 = 0 # soma dos reprovados
j = 0
maior = -1
while(i < size(x)):
	if(x[i] == -1):
		soma = soma + 1
		
	elif(x[i] >= 6):
		soma1 = soma1 + 1
		j = j + x[i]
	if(x[i] != -1 and x[i] < 6):
		soma2 = soma2 + 1
		j = j + x[i]
	if(x[i] == max(x)):
		maior = i
	i = i + 1
c = j/((size(x)) - soma)
print(soma)
print(soma1)
print(soma2)
print(round(c,2))
print(y[maior])