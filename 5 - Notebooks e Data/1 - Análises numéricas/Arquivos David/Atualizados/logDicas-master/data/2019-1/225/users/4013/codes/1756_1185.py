from numpy import*
v = array(eval(input("vetor de inteiros:")))
i = 0 #posicao
acum = 0  #glicose elevada

while(i < size(v)):
	if(v[i] > 99):         
		print(i)
		acum = acum + 1
	i = i + 1
print(acum)	