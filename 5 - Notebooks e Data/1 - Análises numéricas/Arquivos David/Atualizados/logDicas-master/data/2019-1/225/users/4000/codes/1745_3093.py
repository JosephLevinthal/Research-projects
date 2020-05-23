n = input("Resultado das partidas: ")
c=0
soma=0
while(c<n):
	if(n==3):
		soma = soma + 3
		c = c+1
		print(soma, "V")
	elif(n==1):
		soma = soma +1
		c= c+1
		print(soma, "E")
	elif(n==0):
		soma = soma + 0
		c = c+1
		print(soma, "D")
	else:
		print("X")
	
	
	
	
	