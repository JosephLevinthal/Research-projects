from numpy import *

mf = array(eval(input("")))
horas = array(eval(input("")))
carga = int(input(""))

x = zeros(3, dtype = int)
freqmin = carga - (carga/4)

for i in range(size(mf)):
		
	if mf[i] >= 5 and horas[i] >= freqmin:
		x[0] += 1
	elif mf[i] < 5:
		x[1] += 1
	elif horas[i] < freqmin:
		x[2] += 1
	
print(x)