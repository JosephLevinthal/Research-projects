from numpy import *
vetor = array(eval(input("digite os coeficientes: ")))
string = ""
i = 0
s = size(vetor)
while(i<size(vetor)):
	if(s != 2):
		string = string +  str(vetor[i]) + "x^" + str(s-1) + " + "
	else:
		string = string + str(vetor[i]) + "x + "
	i = i  +  1
	s = s - 1
print(string[:-6])
##############