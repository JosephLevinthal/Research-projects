z = int(input("Digite um numero inteiro diferente de zero: "))

n = z
while (n > 1): #condicao para repeticao do laco, enquanto nao se tiver o resultado 1 
	if(n%2 == 0): #verifica se e par
		n = n//2 #executa a condicao se for par
	elif(n%2 != 0): # se não for par = impar
		n = 3*n + 1  #executa a condicao para impar
	print(n)	 #imprime o valor de n