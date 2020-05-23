îfrom math import *

numeroN = int(input("Informe valor de N: "))

# Variaveis do Denominador
cont = 0
expoente = 0

# Variaveis do Restante do Cálculo
resultado = 0
sinal = 1

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

===============

# Instituto de Computacao - UFAM
# Nathaly Leite

from math import *

x = 
k = int(input("Informe um numero K: "))

soma = x
i = 1
sinal = -1
expoente = 3

while (i < k):
	#f = factorial(expoente)
	soma = soma + (sinal * (x ** expoente)) / factorial(expoente)
	sinal = sinal * (-1)
	expoente = expoente + 2
	i = i + 1
	
print (round(soma,10))

===========

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