from numpy import*

vetent = array(eval(input("entrada no onibus: ")))
vetsai = array(eval(input("saida do onibus: ")))

for i in range(size(vetent)):
	for j in range(size(vetsai)):
		
		pessoas = vetent[i]-vetsai[j]
		
print(pessoas)