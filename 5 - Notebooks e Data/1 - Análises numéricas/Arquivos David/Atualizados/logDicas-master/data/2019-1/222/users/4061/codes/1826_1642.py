from numpy import*

turmas = array(eval(input("alunos por turmas: ")))

cont = 0
for i in range(size(turmas)):
	if(turmas[i] % 5 == 0):
		cont = cont + 1
		
cont2 = 0
z = zeros(cont, dtype=int)

for p in range(size(turmas)):
	#z = z + 1
	cont2 = cont2 + 1
	
print(cont)
print(z)