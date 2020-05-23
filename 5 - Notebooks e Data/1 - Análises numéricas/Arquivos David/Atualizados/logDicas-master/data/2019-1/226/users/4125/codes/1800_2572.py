#matricula par grupo 1
#matricula impar grupo 2
from numpy import*
x = array(eval(input("digite a matricula do aluno: ")))
a = 0
for i in x:
	if (i % 2 != 0):
		a = a + 1
grupo2 = zeros(a, dtype = int)
y = 0
y1 = 0
for  j in x:
	if(j % 2 != 0):
		grupo2[y] = x[y1]
		y = y + 1
	y1 = y1 + 1
print(grupo2)