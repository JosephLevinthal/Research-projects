from numpy import*
vet1 = array(eval(input("Insira a quant. de pessoas que entraram no onibus: \n")))
vet2 = array(eval(input("Insira a quant. de pessoas que sairam do onibus: \n")))

i = 0
s = 0 
onibus = 0
while(i < size(vet1)):
	if(vet1[i] <= 75):
		s = 75 - vet2[i]
		onibus = s + vet1[i]
	i = i + 0
print(onibus)
		
	