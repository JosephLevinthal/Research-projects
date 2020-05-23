from math import *
n = int(input("insere o numero natul: "))

cont = 1
i = 3

while (cont < n):
	d = (cont*2) * (cont*2 +1) * (cont*2 +2)
	i = i + (-1)**(cont+1) * 4 / d 
	cont = cont + 1
	
print(round(i,8))