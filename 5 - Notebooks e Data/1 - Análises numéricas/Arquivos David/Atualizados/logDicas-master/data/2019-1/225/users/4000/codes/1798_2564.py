from numpy import*
cont = zeros(3, dtype=int)
gm = array(eval(input("Gols marcados: ")))
gs = array(eval(input("Gols sofridos: ")))
for i in range(size(gm)):
	if(gm[i] > gs[i]):
		cont[0] = cont[0] + 1
	elif(gm[i] == gs[i]):
		cont[1] = cont[1] + 1
	elif(gm[i] < gs[i]):
		cont[2] = cont[2]+1
print(cont)

	
