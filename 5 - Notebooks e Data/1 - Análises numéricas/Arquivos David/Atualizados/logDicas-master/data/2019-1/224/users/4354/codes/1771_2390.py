from numpy import *
pres = array(eval(input("alunos presentes: ")))
fal = array(eval(input("faltas: ")))
#0 = janeiro,1 = fevereiro,...
pf = pres - fal
i = 0

while(i < size(pf)):
	if(pf[i] == max(pf)):
		print(i+1)
	i = i + 1


