from numpy import*

faltas = array(eval(input("faltas:")))
cont = zeros(6)

for i in range(size(faltas)):
	
	if (faltas[i] == 2):
		cont[0] += 1
	
	elif(faltas[i] == 3):
		cont[1] += 1
	
	elif (faltas[i] == 4):
		cont[2] += 1
	
	elif (faltas[i] == 5):
		cont[3] += 1
	
	elif (faltas[i] == 6):
		cont[4] += 1
	
	else:
		cont[5] += 1

for i in range(size(cont)):
	cont[i] = (cont[i] / size(faltas)) * 100 
	cont[i] = round(cont[i],1)

print(cont)	