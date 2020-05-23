from numpy import*
n= array(eval(input("quais as notas dos alunos? ")))
a=0
m=0
a=0
while(size(n)>1):
	a=0
	for i in n:
		if i>=5 and i<7:
			a=a+1
	print(a)

	n= array(eval(input("proximo vetor: ")))
