from numpy import *

turmas = array(eval(input("Alunos por turma: ")))

z = zeros(6, dtype=int)

for i in range(size(v)):
	if turmas[i] % 5 == 0:
		z[0] = z[0] + 1
	elif v[i] == 3:
		z[1] = z[1] + 1
	elif v[i] == 4:
		z[2] = z[2] + 1
	elif v[i] == 5:
		z[3] = z[3] + 1
	elif v[i] == 6:
		z[4] = z[4] + 1
	elif v[i] == 7:
		z[5] = z[5] + 1

		
f = zeros(6)
for p in range(6):
	porcentagem = round(((z[p]/sum(z))*100),1)
	f[p] = porcentagem
	
print(f)