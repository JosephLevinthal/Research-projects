from numpy import*

c = array(eval(input("Vetor: ")))

i = 0
v = 0
n = size(c)
while(i < size(c)):
	v = (c[i]**2) + v
	i = i + 1
cont = (v/n)**(1/2)
print(round(cont, 2))