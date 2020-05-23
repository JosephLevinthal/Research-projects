from numpy import*

d = array(eval(input("Digite as faltas: ")))

cont = zeros(6, dtype = float)

for i in range(size(d)):
	if(d[i] == 2):
		cont[0] = cont[0] + 1
	elif(d[i] == 3):
		cont[1] = cont[1] + 1 
	elif(d[i] == 4):
		cont[2] = cont[2] + 1 
	elif(d[i] == 5):
		cont[3] = cont[3] + 1 
	elif(d[i] == 6):
		cont[4] = cont[4] + 1 
	elif(d[i] == 7):
		cont[5] = cont[5] + 1 	

d = sum(cont)

for i in range(size(cont)):
	cont[i] = (cont[i]/d) * 100
	cont[i] = round(cont[i], 1)

print(cont)	
	
