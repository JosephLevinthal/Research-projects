from numpy import*

gols = array(eval(input("A: ")))
golsadv = array(eval(input("B: ")))

cont = zeros(3, dtype=int)

for i in range(0, size(gols)):
	#vitorias
	if (gols[i]) > golsadv[i]:
		cont[0] = cont[0] + 1 
	#empate
	elif(gols[i] == golsadv[i]):
		cont[1] = cont[1] + 1
	#derrota
	else:
		cont[2] = cont[2] + 1
print(cont)		
