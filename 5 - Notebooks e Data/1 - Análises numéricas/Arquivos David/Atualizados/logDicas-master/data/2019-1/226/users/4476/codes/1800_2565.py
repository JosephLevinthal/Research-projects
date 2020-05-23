from numpy import *
vmf = array(eval(input("digite: ")))
vph = array(eval(input("digite: ")))
vch = int(input("digite: "))

v = zeros(3, dtype=int)

for i in range(size(vmf)) and range(size(vph)):
	ph = (vph[i]*100)/vch
	if (vmf[i] >= 5) and (ph >= 75):
		v[0] = v[0] + 1
	elif (ph >= 75) and (vmf[i] < 5):
		v[1] = v[1] + 1
	elif (ph < 75):
		v[2] = v[2] + 1
	ph=0
print(v)