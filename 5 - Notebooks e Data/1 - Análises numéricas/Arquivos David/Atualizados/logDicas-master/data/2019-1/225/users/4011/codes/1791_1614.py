from numpy import*

nomes = array(eval(input("Nome dos alimentos: ")))
quant = array(eval(input("Grama dos alimentos: ")))

i = 0 
kcal1 = 0
kcal2 = 0
kcal3 = 0
kcal4 = 0
kcal5 = 0

while(i < size(nomes)):
	
	if(nomes[i] == "BANANA"):
		kcal1 = kcal1 + quant[i] * 0.97
	elif(nomes[i] == "BIFE"):
		kcal2 = kcal2 + quant[i] * 2.95
	elif(nomes[i] == "FEIJOADA"):
		kcal3 = kcal3 + quant[i] * 1.27
	elif(nomes[i] == "OMELETE"):
		kcal4 = kcal4 + quant[i] * 1.04
	elif(nomes[i] == "TOMATE"):
		kcal5 = kcal5 + quant[i] * 0.2
	i = i + 1
	
Total = kcal1 + kcal2 +kcal3 + kcal4 +kcal5 

print(round(Total,2))