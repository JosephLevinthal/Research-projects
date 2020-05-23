from numpy import*

vet = array(str(input("Nome do alimento: ")))

vet2 = array(eval(input("Qauntidade:")))


result = zeros(size(vet2))

for i in range(size(vet)):
	if(result[i] == "BANANA"):
		result[i] = round((0.97 * vet2[i]),2)
	elif(result[i] == "BIFE"):
		result[i] = round((2.95 * vet2[i]),2)
	elif(result[i] == "FEIJOADA"):
		result[i] = round((1.27 * vet2[i]),2)
	elif(result[i] == "OMELETE"):
		result[i] = round((1.04 * vet2[i]),2)
	elif(result[i] == "TOMATE"):
		result[i] = round((0.2 * vet2[i]),2)
		
	print(result)
			
		 
		
		
	
