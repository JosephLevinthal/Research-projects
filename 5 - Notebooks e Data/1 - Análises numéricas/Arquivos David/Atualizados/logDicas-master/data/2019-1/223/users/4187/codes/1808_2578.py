from numpy import*
pontos = array(eval(input("potos dos alunos:")))
par = 0
for i in range(size(pontos)):
	if(pontos[i] % 2 == 0):
		par = par + 1
grupo_1 = zeros(par, dtype=int)
i_1 = 0
for i in range(size(pontos)):
	if(pontos[i] % 2 == 0):
		if(i_1 <= size(grupo_1)):
			grupo_1[i_1] = pontos[i] 
			i_1 = i_1 + 1
print(grupo_1)