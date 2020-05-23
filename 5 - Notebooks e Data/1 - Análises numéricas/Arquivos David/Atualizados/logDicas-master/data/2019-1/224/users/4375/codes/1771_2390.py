from numpy import*
aqui=array(eval(input("n de alunos presentes: ")))
vish=array(eval(input("n de alunos faltosos: ")))
pf=aqui-vish
i=0

while(i<size(pf)):
	if(pf[i]== max(pf)):
		print(i+1)
	i=i+1