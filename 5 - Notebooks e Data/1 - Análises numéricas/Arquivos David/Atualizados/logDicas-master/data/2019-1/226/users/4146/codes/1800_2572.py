from numpy import *
alunos = array(eval(input("Matriculas: ")))
n = 0
i = 0

for x in alunos:
	if(x%2 != 0):
		n = n + 1
		
g2 = zeros(n, dtype=int)

for x in alunos:
	if(x%2 != 0):
		g2[i] = g2[i] + x
		i = i + 1
		
print(g2)		
