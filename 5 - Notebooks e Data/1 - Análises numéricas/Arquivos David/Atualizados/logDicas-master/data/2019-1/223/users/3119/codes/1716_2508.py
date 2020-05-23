n = int(input("Digite o numero: "))
i = 3
cont = 1

while(cont < n):
	if(n == 1):
		print(i)
	else:
		den = (cont*2) * (cont*2 + 1) * (cont*2 + 2)
		i = i + (-1)**(cont+1)*4/den
		cont = cont + 1
		
print(round(i,8))		
