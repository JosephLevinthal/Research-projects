from numpy import *

mat = array(eval(input("Matricula dos alunos: ")))
x = zeros(2,dtype=int)

for elemento in mat:
	if (elemento % 2 != 0):
		x[1] = x[1] + 1   # Acumulador dos impares
v = zeros(x[1], dtype=int)
i=0		
for elemento2 in mat:
	if(elemento2 % 2 != 0):
		v[i] = elemento2 
		i = i + 1
print(v)






