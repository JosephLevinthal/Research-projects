from numpy import *

glic = array(eval(input("Valor: ")))

i = 0
c = 0
while(i < size(glic)):
	if (glic[i] > 99):
		print(i)
		c = c + 1
	i = i + 1	
print(c)