from numpy import*
nota= array(eval(input("quais as notas do aluno?")))
freq= array(eval(input("quais as frequencias dos alunos?")))
ch=int(input("qual a carga horaria da materia?"))

vet= zeros(3, dtype=int)

for i in range(size(nota)):
	if (nota[i]>=5 and freq[i]>=(ch*75)/100):
		vet[0]=vet[0]+1
	elif (nota[i]<5 and freq[i]>=(ch*75)/100):
		vet[1]=vet[1]+1
	elif(nota[i]>5 and freq[i]<(ch*75)/100):
		vet[2]=vet[2]+1
print(vet)