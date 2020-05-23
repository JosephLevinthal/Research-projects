from math import *
#Entrada dos dados:
x = eval(input("Digite o angulo de x, em radianos: "))
k = int(input("Digite um numero natural maior do que zero: "))

senx = x #apenas o primeiro termo da seria, se o usuario pedir apenas um termo, o laco nao eh executado
# tambem acumula os valores para x>1 termos
i = 1 #incremento no numero de termos, e tambem contadora dos termos
while(i < k): #condicao do laco: o nume te termos eh inferiro ao numero pedido pelo usuario
	soma = ((-1)**i)*(x**(2*i+1))/factorial(2*i+1) # o sinal e alternado e isso varia em funcao do i, 
	#se i eh impar, o termo e negativo, se i e par o termos eh positivo.
	#2i+1 calcula o expoente e o denominador, em funcao do i termos
	senx = senx + soma #incremento do valor de pi, em funcao da aproximação pedida
	i = i+1
print(round(senx, 10))
