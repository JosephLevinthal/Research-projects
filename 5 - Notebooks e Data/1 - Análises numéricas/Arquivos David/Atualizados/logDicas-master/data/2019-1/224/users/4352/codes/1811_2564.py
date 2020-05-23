from numpy import*
gp = array(eval(input("digite os gols do time em cada partida: ")))
ga = array(eval(input("digite os gols do time adversario: ")))
cont = zeros(3, dtype=int)
for i in range(size(gp)): 
	if gp[i] > ga[i]:
		cont[0] = cont[0] + 1
	elif gp[i] == ga[i]:
		cont[1] = cont[1] + 1
	elif gp[i] < ga[i]:
		cont[2] = cont[2] + 1
print(cont)