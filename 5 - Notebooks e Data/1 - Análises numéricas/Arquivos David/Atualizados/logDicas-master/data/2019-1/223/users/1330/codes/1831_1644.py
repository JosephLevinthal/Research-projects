from numpy import *
aluno = array(eval(input()))
ap = 0
rep = 0
#novovet = zeros(size(aluno), dtype=int)
for i in range(size(aluno)):
	if(aluno[i]>=5.0):
		ap = ap + 1
	else:
		rep = rep + 1
#		novovet[i] = aluno[i]
print(rep)
#print(novovet)
novovet = zeros(rep, dtype=int)
posicao = 0
for i in range(size(novovet)):
	if(aluno[i]<5.0):
		novovet[i] = posicao
	posicao = posicao + 1
print(novovet)
	#posicao = posicao + 1