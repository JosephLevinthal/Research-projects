from numpy import *
v1 = array(eval(input("Total de gols: "))) 
v2 = array(eval(input("Gols sofridos: ")))
vn = zeros(3, dtype = int)

for i in range(size(v1)):
	if(v1[i] > v2[i]):
		vn[0] = vn[0] + 1
	elif(v1[i] == v2[i]):
		vn[1] = vn[1] + 1
	elif(v1[i] < v2[i]):
		vn[2] = vn[2] + 1
print(vn)