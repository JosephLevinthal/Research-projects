from numpy import *
faltas = array(eval(input("Faltas: ")))
n = zeros(6)
for x in faltas:
	if(x == 2):
		n[0] = n[0] + 1
	elif(x == 3):
		n[1] = n[1] + 1
	elif(x == 4):
		n[2] = n[2] + 1
	elif(x == 5):
		n[3] = n[3] + 1
	elif(x == 6):
		n[4] = n[4] + 1
	else:
		n[5] = n[5] + 1
		
for i in range(size(n)):
	if(n[i] > 0):
		n[i] = round((n[i]/size(faltas)) * 100, 1)
		
print(n)		
		