from numpy import*
v = array(eval(input("Primeiro vetor: ")))
while (size(v) > 1):
	alunos = 0
	for i in v:
		if(i>=5 and i <7):
			alunos = alunos + 1
	print(alunos)		
	v = array(eval(input("Proximo vetor: ")))