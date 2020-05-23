n = int(input("Digite um numero: "))

pi = 0 

while(n >= 1):
	if(n % 2 == 1):
		pi = pi + (4/(2*n-1)) #se for impar 
	else:
		pi = pi - (4/(2*n-1)) #se for par0
		
	n = n - 1
	
print(round(pi, 8))
		