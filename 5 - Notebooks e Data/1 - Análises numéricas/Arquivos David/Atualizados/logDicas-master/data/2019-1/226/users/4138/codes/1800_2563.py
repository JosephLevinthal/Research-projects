from numpy import *
#vetor notas
notas = array(eval(input("insira:")))

#laço
while(size(notas)> 2):
	aprov = 0
	
#condiçao
	for x in notas:
		if(x >=5 and x < 7):
			aprov = aprov + 1
	print(aprov)
	notas = array(eval(input("insira as notas:")))
