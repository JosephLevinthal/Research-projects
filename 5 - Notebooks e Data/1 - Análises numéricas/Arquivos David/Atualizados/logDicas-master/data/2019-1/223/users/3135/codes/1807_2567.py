from array import*
n= int(input("Insira o numero:"))

for i in range(n):
	for j in range(n-i):
		print("*", end='')
	print('')
for i in range(n):
	for j in range(1+i):
		print("*", end='')
	print('')