n = int(input("valor de n: "))
i = 1
valor = n
while(i<n):
	if(n%i == 0):
		valor = valor/i
		i = i+1
		#print(valor)
	else:
		valor = valor%i
		i=i+1
print(valor)
	