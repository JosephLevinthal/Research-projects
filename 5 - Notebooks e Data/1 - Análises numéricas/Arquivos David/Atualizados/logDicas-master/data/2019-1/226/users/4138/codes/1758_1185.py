from numpy import *
glicose = array(eval(input("insira o nivel de glicose:")))

i = 0
j = 0
while(i < size(glicose)):
	if(glicose[i]> 99):
		print(i)
		j = j + 1
	i = i + 1
print(j)
		