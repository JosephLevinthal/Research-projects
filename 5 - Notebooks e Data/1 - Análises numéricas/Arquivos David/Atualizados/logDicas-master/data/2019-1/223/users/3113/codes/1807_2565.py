from numpy import*

a=array(eval(input("medias finais de cada aluno: ")))
b=array(eval(input("presenca dos alunos em uma disciplina: ")))
c=int(input("carga horaria da disciplina: "))
vet=zeros(3,dtype=int)
d=c*75
p=d//100

for i in range(size(a)):
	if(a[i]<5):
		vet[1]=vet[1]+1
	elif(b[i]<p):
		vet[2]=vet[2]+1
	elif(a[i]>=5 and b[i]>=p):
		vet[0]=vet[0]+1
print(vet)
