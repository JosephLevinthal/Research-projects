from numpy import *

v = array(eval(input("Insira os gols efetuados:")))
u = array(eval(input("iInsira o numero de gols sofridos:")))

cont = zeros(3,dtype = int)

for i in range(size(v)):
	if(v[i] > u[i]):
		cont[0] = cont[0] + 1
	elif(v[i] == u[i]):
		cont[1] = cont[1] + 1
	elif(v[i] < u[i]):
		cont[2] = cont[2] + 1

print(cont)