from numpy import*
mf=array(eval(input("escreva as medias finais dos alunos: ")))
f=array(eval(input("digite o numero de horas em sala de cada aluno: ")))
ch=float(input("digite o numero de horas: "))
v=zeros(3, dtype=int)
r=ch*75/100
for i in range(size(mf)):
	if(mf[i]>=5) and (f[i]>=r):
		v[0]=v[0]+1
	if(mf[i]<5):
		v[1]=v[1]+1
	if(f[i]<r):
		v[2]=v[2]+1
print(v)