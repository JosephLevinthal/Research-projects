from numpy import * 
vet = array(eval(input("string:"))).split
total = 0
x = zeros(vet, dtype = int)

for i in range(size(vet)):
	if(vet[0] == BE):
		total= total + 1
	elif(vet[1] == ES):
		total= total + 1
	elif(vet[2] == FR):
		total = total + 1
	elif(vet[3] == IT):
		total= total + 1
	elif(vet[4] == PT):
		total = total + 1 
print(max(vet))