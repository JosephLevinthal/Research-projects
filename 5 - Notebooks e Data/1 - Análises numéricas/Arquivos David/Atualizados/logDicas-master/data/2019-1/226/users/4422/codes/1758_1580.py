from numpy import*
notas = array(eval(input("Informe as notas: ")))
nome = array(eval(input("nome: ")))

i = 0
f = 0
a = 0
r = 0
soma = 0
m = -1

while(i < size(notas)):
	if(notas[i] == -1):
		f = f + 1
	elif(notas[i] >= 6):
		a = a + 1
	elif(notas[i] < 6 and notas[i] != -1):
		r = r + 1
	if notas[i] != -1:
		soma = soma + notas[i]
	if notas[i] == max(notas):
		maior = i
	i = i + 1
print(f)
print(a)
print(r)
med = soma / (size(notas) - f)
print(round(med, 2))
print(maior(nome))

