from math import*
x = eval(input("x: "))
k = int(input("k: "))
f = 0
t = -1
g = 1
cont = x
while(f<=k):
	cont =cont + (t*((x**g)/factorial(g)))
	t = t*-1
	f = f+1
	g = g+2
print(round(cont, 10))
	
	
	