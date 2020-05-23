from numpy import *
v1 = array(eval(input("Digite: ")))
cont = 0
cont1 = 0
while (cont < size(v1)):
	if (v1[cont] >= 0):
		cont1 = cont1 + 1
	cont = cont + 1
v2 = arange(cont1)
cont = 0
cont2 = 0
while (cont < size(v1)):
	if (v1[cont] >= 0):
		v2[cont2] = v1[cont]
		cont2 = cont2 + 1
	cont = cont + 1
print(v2)
	