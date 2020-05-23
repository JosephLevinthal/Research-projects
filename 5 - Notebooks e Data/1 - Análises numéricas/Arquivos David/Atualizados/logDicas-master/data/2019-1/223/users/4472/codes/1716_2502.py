from math import *

numeroN = int(input("Informe valor de N: "))

# Variaveis do Denominador
cont = 0 # Variavel contadora
expoente = 0 # Variavel do expoente

# Variaveis do Restante do Cálculo
resultado = 0
sinal = 1 # altera sinal

while (cont < numeroN):
	# Denominador
	denominador = ((2 * cont) + 1) * (3 ** expoente)
	
	# Calculo com as demais variaveis
	calculo = (sqrt(12)) * (sinal * 1) / denominador
	
	resultado = resultado + calculo 
	cont= cont+1
	sinal = sinal * (-1)
	expoente = expoente + 1
	
print(round(resultado, 8))