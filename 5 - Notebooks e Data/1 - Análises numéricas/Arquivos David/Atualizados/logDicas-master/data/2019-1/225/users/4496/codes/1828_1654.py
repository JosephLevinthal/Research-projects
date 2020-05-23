from numpy import*
n = input("Estado de origem: ").split(',')
AM = 0
PE = 0
MG = 0
SP = 0
RS = 0

for i in range(size(n)):
	if(n[i] == AM):
		AM = AM + 1
	elif(n[i] == PE):
		PE = PE + 1
	elif(n[i] == MG):
		MG = MG + 1
	elif(n[i] == SP):
		SP = SP + 1
	elif(n[i] == RS):
		RS = RS + 1
		
a = 0
b = zeros(n, dtype = int)
print(a)
print(b)