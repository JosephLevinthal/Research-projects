# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

raio = float(input("Digite o raio: "))
altura = float((input("Digite a altura de a: ")))
numero = float(input("Digite a opcao 1 ou 2: "))

if( numero == 1):
	v =( ( pi * ( altura ** 2 ) ) * ( 3 * raio - altura) ) / 3

if(numero == 2):
	v =( ( 4 * pi * ( raio ** 3 ) ) / 3 ) - ( ( pi * ( altura ** 2 ) ) * ( 3 * raio - altura) ) / 3
 	
print(round(v,4))

