# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math

raio = float(input())

altura = float(input())

numero = int(input())

volumeAr = ((math.pi * (altura**2)) * (3*raio - altura)) / 3

volumeComb = ((4*(math.pi)) * (raio**3)) / 3

va = round(volumeAr, 4)

vc = round(volumeComb, 4)

combustivel = volumeComb - volumeAr

comb = round(combustivel, 4)

if( numero == 1):
	print(va)
elif (numero == 2):
	print(comb)