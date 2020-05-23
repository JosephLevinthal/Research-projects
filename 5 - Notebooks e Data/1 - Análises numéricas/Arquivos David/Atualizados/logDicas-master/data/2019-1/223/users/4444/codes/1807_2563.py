from numpy import *
notas = array(eval(input("Notas: "))) #vetor contendo as notas médias dos alunos

while(size(notas)>1):          
	n_monitor = 0
	for elemento in notas:
		if(5 <= elemento < 7):
			n_monitor= n_monitor + 1
	print(n_monitor)
	notas = array(eval(input("proximas notas: ")))		

