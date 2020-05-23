from numpy import *

v = array(eval(input("insira os numeros:")))

cont = zeros(4,dtype =int)

for i in range(size(v)):
	if(v[i] == 1):
		cont[0] = cont[0] + 1
	elif(v[i] == 2):
		cont[1] = cont[1] + 1
	elif(v[i] == 3):
		cont[2] = cont[2] + 1
	elif(v[i] == 4):
		cont[3] = cont[3] + 1
print(cont)