from numpy import *
pre = array(eval(input("alunos presentes: ")))
fa = array(eval(input("faltas: ")))
#0 = janeiro,1 = fevereiro,...
f = pre - fa
i = 0

while(i < size(f)):
	if(f[i] == max(f)):
		print(i+1)
	i = i + 1


