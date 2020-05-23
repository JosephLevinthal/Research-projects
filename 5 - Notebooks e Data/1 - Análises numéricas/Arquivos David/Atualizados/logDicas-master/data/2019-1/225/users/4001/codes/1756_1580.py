from numpy import *
v = array(eval(input("notas: ")))
n = array(eval(input("nomes: ")))
v1 = 0 #qtd de aprov
v2 = 0 #qtd de reprov
i = 0 #contadora
f = 0 #faltas
p = 0 #presentes
soma = 0
while (i < size(v)):
	if (v[i] > -1):
		if (v[i] >= 6 and v[i] <= 10):
			v1 = v1 + 1
			soma = soma + v[i]
		elif (v[i] < 6):
			v2 = v2 + 1
			soma = soma + v[i]
		p = p + 1 
	if (v[i] == -1):
		f = f + 1
	i = i + 1
i = 0
while (v[i] != max(v)):
	i = i + 1

print(f)
print(v1)
print(v2)
print(round(soma/(v1 + v2), 2))
print(n[i])

		
	
		