from numpy import*
v=array(eval(input("insira a quantidade de alunos matriculados em cada turma:  ")))
q=size(v)
va=0
s=0
for i in range(q):
	if v[i]%5==0:
		va=va+1
v0=zeros(va, dtype=int)
for j in range(q):
	if v[j]%5==0:
		v0[s]=j
		s=s+1
print(va)
print(v0)