from numpy import*
v1 = array(eval(input("Quantidade de alunos por turma: ")))
par = 0

for i in range(size(v1)):
	if( i % 2 == 0):
		par = par + 1
	
r = array(zeros(par), dtype=int)
	
for i in range(size(v1)):
	r[1] = r[1] + 1
	
	
print(par)
print(r) #2 - vetores pares [n x y]