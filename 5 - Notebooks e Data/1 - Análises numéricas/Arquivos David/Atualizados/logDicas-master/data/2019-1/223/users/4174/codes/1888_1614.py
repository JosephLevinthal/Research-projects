from numpy import*

alimento = array(eval(input("nomes dos alimentos:")))
grama = array(eval(input("kcal por grama:")))

quantidade = zeros(size(alimento))
for i in range(size(alimento)):
	if(alimento[i] == "BANANA"):
		quantidade[i] = round((0.97 * grama[i]),2)	
	elif(alimento[i] == "BIFE"):
		quantidade[i] = round((2.95* grama[i]),2)
	elif(alimento[i] == "FEIJOADA"):
		quantidade[i] = round((1.27* grama[i]),2)
	elif(alimento[i] == "OMELETE"):
		quantidade[i] = round((1.04* grama[i]),2)
	elif(alimento[i] == "TOMATE")	:
		quantidade[i] = round((0.2 *grama[i]),2)
		

print(sum(quantidade))	
		
	
				 


