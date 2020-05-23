from numpy import *
gols_feitos = array(eval(input("digite o vetor :")))
gols_sofridos = array(eval(input("digite o vetor :")))
i = 0
v = 0
e = 0
d = 0
while(i<size(gols_feitos)):
	if(gols_feitos[i] - gols_sofridos[i] == 0):
		i = i + 1
		e = e + 1
	elif(gols_feitos[i] > gols_sofridos[i]):
		i = i + 1
		v = v + 1
	else:
		i = i + 1
		d = d + 1
z = ones(3,dtype = int)
z[0]=v
z[1]=e
z[2]=d
print(z)

