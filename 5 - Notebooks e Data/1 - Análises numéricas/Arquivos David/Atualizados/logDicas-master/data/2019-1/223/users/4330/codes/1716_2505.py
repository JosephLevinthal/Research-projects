from math import*
x = eval(input("Digite: "))
k = int(input("Digite um valor: "))
contador = 1
sinal =-1 
resultado = x
expoente = 3
while ( contador < k  ):
	resultado = resultado + ( sinal * ( x ** expoente/factorial(expoente)))
	sinal = sinal*(-1)
	expoente = expoente + 2
	contador += 1 
print(round(resultado,10))
