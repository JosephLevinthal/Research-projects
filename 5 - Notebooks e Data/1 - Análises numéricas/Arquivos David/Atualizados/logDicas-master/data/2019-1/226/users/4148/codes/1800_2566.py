from numpy import*

v = array(eval(input("faltas: ")))

cont = zeros(6, dtype=float)

for i in range(size(v)):
	if v[i] == 2:
		cont[0] = cont[0] + 1
		
	elif v[i] == 3:
		cont[1] = cont[1] + 1
		
	elif v[i] == 4:
		cont[2] = cont[2] + 1
	
	elif v[i] == 5:
		cont[3] = cont[3] + 1 
		
	elif v[i] == 6:
		cont[4] = cont[4] + 1
		
	elif v[i] == 7:
		cont[5] = cont[5] + 1
		
cont[0] = round((cont[0]/size(v)) * 100, 1)
cont[1] = round((cont[1]/size(v)) * 100, 1)		
cont[2] = round((cont[2]/size(v)) * 100, 1)
cont[3] = round((cont[3]/size(v)) * 100, 1)
cont[4] = round((cont[4]/size(v)) * 100, 1)
cont[5] = round((cont[5]/size(v)) * 100, 1)

print(cont)