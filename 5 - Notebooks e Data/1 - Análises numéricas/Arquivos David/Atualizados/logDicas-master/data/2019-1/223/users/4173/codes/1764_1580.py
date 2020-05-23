from numpy import*
va = array(eval(input()))
vb = array(eval(input()))
k = 0
notas = 0
faltaram = 0
aprovados = 0
reprovados = 0
alunos = 0
while k < size(va):
	if (va[k] == -1):
		faltaram +=1
	if (va[k] >= 6):
		aprovados +=1
	if (va[k] < 6) and (va[k] > -1):
		reprovados +=1
	if (va[k] > -1):
		alunos +=1
		notas += va[k]
	if va[k] == max(va):
		x = vb[k]
		
	k +=1
l = notas/alunos
print(faltaram)
print(aprovados)
print(reprovados)
print(round(l,2))
print(x)