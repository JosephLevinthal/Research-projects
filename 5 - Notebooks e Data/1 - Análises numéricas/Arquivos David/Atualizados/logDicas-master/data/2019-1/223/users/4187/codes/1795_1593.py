from numpy import*
notas = array(eval(input("notas:")))
peso1 = arange(size(notas))

i = 0
soma_nota = 0
while(i < size(peso1)):
	peso1[i] = peso1[i] + 1
	i = i + 1
i = 0 
while(i < size(notas)):
	soma_nota = soma_nota + (notas[i] * peso1[i])
	i = i + 1
soma_dos_pesos = sum(peso1)
print(round(soma_nota/soma_dos_pesos, 2))