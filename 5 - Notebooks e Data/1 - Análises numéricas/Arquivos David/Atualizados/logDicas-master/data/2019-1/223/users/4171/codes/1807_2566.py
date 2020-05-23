from numpy import *

dia = array(eval(input("Dias em que o empregado faltou: ")))
z = zeros(6)

for i in range(size(dia)):
	if dia[i] == 2:
		z[0] += 1
	elif dia[i] == 3:
		z[1] += 1
	elif dia[i] == 4:
		z[2] += 1
	elif dia[i] == 5:
		z[3] += 1
	elif dia[i] == 6:
		z[4] += 1
	elif dia[i] == 7:
		z[5] += 1

for k in range(size(z)):
	
	z[k] = (z[k]/size(dia)) * 100
	z[k] = round(z[k],1)
	
print(z)