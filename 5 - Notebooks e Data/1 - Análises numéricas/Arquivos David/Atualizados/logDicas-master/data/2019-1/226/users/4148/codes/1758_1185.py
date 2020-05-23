from numpy import*

g = array(eval(input("g: ")))

i = 0
cont = 0

while(i < size(g)):
	if(g[i]>99):
		print(i)
		cont = cont + 1
	i = i + 1
print(cont)