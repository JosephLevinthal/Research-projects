from numpy import*
f = array(eval(input("digite as faltas: "))) #de 2 a 7
cont = zeros(6, dtype=int)
for i in range(size(f)): 
	if f[i] == 2:
		cont[0] = cont[0] + 1
	elif f[i] == 3:
		cont[1] = cont[1] + 1
	elif f[i] == 4:
		cont[2] = cont[2] + 1
	elif f[i] == 5:
		cont[3] = cont[3] + 1
	elif f[i] == 6:
		cont[4] = cont[4] + 1
	elif f[i] == 7:
		cont[5] = cont[5] + 1
nv = zeros(6, dtype=float)
for i in range(size(nv)):
	nv[i] = round((cont[i]/(size(f)))*100, 1)
print(nv)