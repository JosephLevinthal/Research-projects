from numpy import *

v1 = array(eval(input("Insira as medias finais: ")))
v2 = array(eval(input("Insira a frequencia: ")))
v3 = int(input("Insira a carga horaria: "))

x = zeros(3,dtype=int)
f = v3*(0.75)
for i in range(size(v1)):
	if((v1[i] >= 5) and (v2[i] >= f)):
		x[0] = x[0] + 1
	elif((v1[i] < 5) and (v2[i] >= f)):
		x[1] = x[1] + 1
	elif((v1[i] >= 5) and (v2[i] < f)):
		x[2] = x[2] + 1
print(x)