from numpy import*

mat_string = input('Matriculas: ')
mat_vetor = mat_string.split(',')

num_alunos = size(mat_vetor)

k = 0
v = zeros(num_alunos)

while k < num_alunos:
	v[k] = int(input("Numero de faltas aluno: "))
	k = k + 1
	
matriz = zeros((num_alunos, 2), dtype=int)

for i in range(num_alunos):
	matriz[i, 0] = mat_vetor[i]
	matriz[i, 1] = v[i]

for j in range(num_alunos):
	if v[j] == max(v):
		jmin = j

min_aluno = mat_vetor[jmin]

print(matriz)
print("O aluno que possui o maior numero de faltas e o",min_aluno)