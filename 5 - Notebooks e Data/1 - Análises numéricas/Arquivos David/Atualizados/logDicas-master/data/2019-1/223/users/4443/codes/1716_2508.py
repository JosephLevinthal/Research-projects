#Entrada dos dados:
n = int(input("Digite um numero: "))
pi = 3.0 #primeiro valor da serie, se o usuario pedir 1 termo, o laco nao eh executado
#tambe é acumuladora do valor aproximado, a partir do primeiro termo
i = 1 #acumuladora dos i termos a parti do primeiro
while(i < n): # condicao do laco, i termos menor do que o pedido pelo usuario
	d = (2*i)*(2*i+2)*(2*i+1) #denominador cresce em funcao do i
	parcela = -1*((4*(-1)**i)/d) # o -1 serve para transformar o primeiro termo com positivo e o segundo negativo
	pi = pi + parcela #atualiza o valor de pi
	i = i + 1 #incremento do numero de termos
	
print(round(pi,8))	