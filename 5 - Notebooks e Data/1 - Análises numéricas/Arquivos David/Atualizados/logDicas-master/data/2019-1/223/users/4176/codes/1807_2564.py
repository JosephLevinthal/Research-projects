from numpy import*
gols = array(eval(input("Digite: ")))
gols2 = array(eval(input("Digite: ")))
resultado = zeros(3, dtype=int)

for i in range(0,size(gols)):
	if(gols[i] > gols2[i]):
		resultado[0] = resultado[0] + 1
	elif(gols[i] == gols2[i]):
		resultado[1] = resultado[1] + 1
	elif(gols[i] < gols2[i]): 
		resultado[2] = resultado[2] + 1
		
print(resultado)
		
	


