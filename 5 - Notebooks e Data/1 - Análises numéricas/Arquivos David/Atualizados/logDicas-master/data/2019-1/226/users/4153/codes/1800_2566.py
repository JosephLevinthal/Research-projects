from numpy import *

v = array(eval(input("Insira o historico de faltas: ")))
x = zeros(6, dtype=float)

for i in range(size(v)):
	if(v[i] == 2):
		x[0] = x[0] + 1
	elif(v[i] == 3):
		x[1] = x[1] + 1
	elif(v[i] == 4):
		x[2] = x[2] + 1
	elif(v[i] == 5):
		x[3] = x[3] + 1
	elif(v[i] == 6):
		x[4] = x[4] + 1
	elif(v[i] == 7):
		x[5] = x[5] + 1

x = (x/size(v)) * 100
for r in range(size(x)):
	x[0] = round(x[0], 1)
	x[1] = round(x[1], 1)
	x[2] = round(x[2], 1)
	x[3] = round(x[3], 1)
	x[4] = round(x[4], 1)
	x[5] = round(x[5], 1)
print(x)