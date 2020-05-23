from numpy import *
n = zeros(6, dtype = float)
v = array(eval(input("Faltas: ")))
for i in range(size(v)):
	if(v[i] == 2):
		n[0] = n[0] + 1
	elif(v[i] == 3):
		n[1] = n[1] + 1
	elif(v[i] == 4):
		n[2] = n[2] + 1
	elif(v[i] == 5):
		n[3] = n[3] + 1
	elif(v[i] == 6):
		n[4] = n[4] + 1
	elif(v[i] == 7):
		n[5] = n[5] + 1
for k in range(size(n)):
	n[k] = round(n[k]/size(v) * 100, 1)
print(n)
