n = int(input("Digite um numero: ")) #entrada do numero de repeticoes
a = "*" #variavel que armazena o ch que sera repetido
b = "o" #variavel que armazena o ch que sera repetido

for i in range(n): #para cada posicao da variacao de 0 a n
	print(a*(n-i)+b*(2*i)+a*(n-i)) 
	