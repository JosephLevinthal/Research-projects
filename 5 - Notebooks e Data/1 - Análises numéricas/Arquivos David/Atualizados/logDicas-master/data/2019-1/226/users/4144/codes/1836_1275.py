from numpy import *
mat = array(eval(input("digite a matriz: ")))
funcionario = shape(mat)[0]
horas = zeros(funcionario, dtype=int)
for i in range(funcionario):
	horas[i]=sum(mat[i,:])
print(horas)