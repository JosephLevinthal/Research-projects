from numpy import *
glic = array(eval(input("Digite ")))

i = 0
acima = 0
while (i < size(glic)):
	if (glic[i] > 99):
		print(i)
		acima += 1
	i += 1
print(acima)