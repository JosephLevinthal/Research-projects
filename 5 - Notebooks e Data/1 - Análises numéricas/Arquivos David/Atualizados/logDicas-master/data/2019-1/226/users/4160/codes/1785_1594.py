from numpy import *
#vetor de danos
vd = array(eval(input("Vetor de danos: ")))
#ataque 1 = v[0]*1
#ataque 2 = v[i] + 1

i = 0  #cont laco posicao
f = 0 #peso
soma = 0
while(i<size(vd)):
	i = i + 1
	f = f + 1
	soma=soma+1
	w = vd[i] + vd[i] * f

y=sum(w)

print(y)

