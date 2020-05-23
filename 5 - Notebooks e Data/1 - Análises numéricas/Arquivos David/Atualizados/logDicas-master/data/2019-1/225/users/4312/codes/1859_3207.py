from numpy import*
q_t =int(input("Quant. de turmas: "))
q_a = int(input("Quant. de alunos "))
li_al = array(eval(input("Lista de alunos: ")))
y = q_t*q_a

mat = zeros(y).split(',')

for i in range(y):
	for j in range(y):
		mat[i] = li_al[i]
	li_al = array(eval(input("Insira novamente a lista: ")))

print(mat)
print(size(mat))