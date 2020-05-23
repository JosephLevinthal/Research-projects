from numpy import*

mf= array(eval(input("insira as medias finais de cada aluno: ")))
p= array(eval(input("insira a presenca (numero de horas) dos alunos em uma disciplina: ")))
ch=array(eval(input("insira a carga horaria da disciplina: ")))

z= zeros(3, dtype=int)
a=0
rn=0
rf=0

for i in range(size(mf)):
	if p[i]>=((75/100)*ch) and mf[i]>=5:
		z[0]=z[0]+1
	elif mf[i]<5:
		z[1]=z[1]+1
	elif p[i]<((75/100)*ch):
		z[2]=z[2]+1
print(z)