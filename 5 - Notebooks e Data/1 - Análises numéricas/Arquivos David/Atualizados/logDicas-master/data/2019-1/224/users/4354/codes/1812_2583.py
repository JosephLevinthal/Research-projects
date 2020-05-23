from numpy import *
inter1 = int(input('digite o primeiro intervalo: '))
inter2 = int(input('digite o segundo intervalo: '))
for i in range(inter2):
	if(inter1 <= i*6 <= inter2):
		print(i*6)