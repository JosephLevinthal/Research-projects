from math import *
x = int(input("Digite o numero de pontas da estrela: "))


i = 4
while(i <= x):
	if(i%2 != 0):
		p = (sin(pi/i))/sin((3*pi)/(2*i))
	else:
		p = (sin(pi/i))/sin((2*pi)/i)
	p = round(p, 4)	
	print(i, p)
	i = i+1
	
		