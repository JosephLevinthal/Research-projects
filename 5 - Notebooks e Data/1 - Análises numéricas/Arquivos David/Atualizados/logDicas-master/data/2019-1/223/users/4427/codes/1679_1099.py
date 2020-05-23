# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

from math import *

A = float(input("Lado 1: "))
B = float(input("Lado 2: "))
C = float(input("Lado 3: "))

print("Entradas:", A, ",", B, ",", C)

if (A + B > C):
   if (A == B) and (A == C):
      print ("Tipo de triangulo: equilatero")
   elif (A == B) or (B == C) or (A == C):
      print ("Tipo de triangulo: isosceles")
   elif A != B and C or B != A and C or A != C:
      print ("Tipo de triangulo: escaleno")
else:
	print ("Tipo de triangulo: invalido")
	
	
	
