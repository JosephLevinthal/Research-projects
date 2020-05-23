n = int(input())
formula = 3
cont = 2
denominador = 0
i = 2
if(n==1):
	print(round(formula,8))
else:
	while (1):
		if(i==n+1):
			break
		denominador = cont * (cont+1) *(cont+2)
		if(i % 2 !=0 and i>1): #se o termo for impar, é pra diminuir
			formula -= 4/denominador 
		else:
			formula += 4/denominador
		cont += 2
		i = i+1
	print(round(formula,8))