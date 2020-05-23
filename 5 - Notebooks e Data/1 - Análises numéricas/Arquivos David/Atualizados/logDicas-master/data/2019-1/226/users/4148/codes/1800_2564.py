from numpy import*

v1 = array(eval(input("numero de gols: ")))
v2 = array(eval(input("numero de gols do adversario: ")))


cont = zeros(3, dtype=int)

for i in range(size(v1)):
	if v1[i] > v2[i]:
		cont[0] = cont[0] + 1
		
	elif v1[i]==v2[i]:
		cont[1] = cont[1] + 1
		
	elif v1[i]<v2[i]:
		cont[2] = cont[2] + 1
		
print(cont)   
	