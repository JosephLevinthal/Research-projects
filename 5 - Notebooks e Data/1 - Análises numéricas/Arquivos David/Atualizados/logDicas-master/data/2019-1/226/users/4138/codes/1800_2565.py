from numpy import *
v = array(eval(input("insira as medias finais de cada aluno:")))
u = array(eval(input("insira as horas frequentadas:")))
w = int(input("insira a carga horaria:"))

cont = zeros(3,dtype = int)

for i in range(size(v)):
	a = (u[i]/w) *100
	if(v[i] >= 5 and a >= 75):
		cont[0] = cont[0] + 1
	elif(v[i] < 5 and a >= 75):
		cont[1] = cont[1] + 1
	elif(a < 75):
		cont[2] = cont[2] + 1

print(cont)
	
