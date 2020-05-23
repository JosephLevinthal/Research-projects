from numpy import*
v1 = array(eval(input("digite as notas: ")))
v2 = array(eval(input("digite o nome: ")))
i = 0 #contador do vetor
a = 0 #aprovados
reprov = 0
fault = 0
soma = 0
maior = -1
while(i<size(v1)):
	if(v1[i]==-1):
		fault = fault + 1
	elif(v1[i]>=6):
		a = a + 1
	elif(v1[i]<6)and (v1[i]!=-1):
		reprov = reprov + 1
	if(v1[i]!=-1):
		soma = soma + v1[i]
	if v1[i]==max(v1):
		maior = i
	i = i + 1
print(fault)
print(a)
print(reprov)
print(round((soma/(size(v1)-fault)),2))
print(v2[maior])