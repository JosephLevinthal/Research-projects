from array import*
a= int(input("Insira o numero:"))

for i in range(a):
	for j in range(a-i):
		print("*", end='')
	print('')
for i in range(a):
	for j in range(1+i):
		print("*", end='')
	print('')
