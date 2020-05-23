
from numpy import *
from numpy.linalg import *
# Respostas dos alunos às questões
resp = array ([
['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']])

# Gabarito das questões
gab = array(
['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D'])

nalunos=shape(resp)[0]
nquestoes=shape(resp)[1]
notas=zeros((nalunos), dtype=int)
for i in range(nalunos):
	for j in range(nquestoes):
		if resp[i,j]==gab[j]:
			notas[i]=notas[i]+1
print(notas)
print(dot(notas,notas.T))