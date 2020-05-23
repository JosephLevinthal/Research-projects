from numpy import *

v = array(eval(input("insira os dias de falta:")))
					
cont = zeros(6,dtype = float)
					
for i in range(size(v)):
	if(v[i] == 2):
		cont[0] =  cont[0] + 1
	elif(v[i] == 3):
		cont[1] = cont[1] + 1
	elif(v[i] == 4):
		cont[2] = cont[2] + 1
	elif(v[i] == 5):
		cont[3] = cont[3] + 1
	elif(v[i] == 6):
		cont[4] = cont[4] + 1
	elif(v[i] == 7):
		cont[5] = cont[5] + 1
					
for i in range(size(cont)):
	cont[i] = round((cont[i]/size(v))*100,1)

print(cont)




