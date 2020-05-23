from numpy import*
from numpy.linalg import*
m = array(eval(input("digite uma matriz de notas: ")))
linha = m.shape[0]
coluna = m.shape[1]
cont = 0
soma = 0
for i in range(linha):
	media=sum(m[i,:])/coluna
	if media > 5.0:
		cont = cont + 1
print(cont)
