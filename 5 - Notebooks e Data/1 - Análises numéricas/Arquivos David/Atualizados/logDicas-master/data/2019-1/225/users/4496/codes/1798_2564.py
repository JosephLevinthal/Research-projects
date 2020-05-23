from numpy import*
cont = zeros(3, dtype=int)

gf = array(eval(input("Gols marcados: ")))
gs = array(eval(input("Gols sofridos: ")))

for x in range(size(gf)):
	if (gf[x] > gs[x]):
		cont[0] = cont[0] + 1
	elif (gf[x] == gs[x]):
		cont[1] = cont[1] + 1
	elif (gf[x] < gs[x]):
		cont[2] = cont[2] + 1
						  
print(cont)


