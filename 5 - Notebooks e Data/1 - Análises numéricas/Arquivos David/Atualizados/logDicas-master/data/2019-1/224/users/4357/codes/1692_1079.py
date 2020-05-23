# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
s = (a + b + c) / 2.0
area = sqrt(s * (s-a) * (s-b) * (s-c))
area = round(area, 3)
mensagem="invalida"

if (a>=b+c) or (b>=a+c) or (c>=b+a) or (a<0) or (b<0) or (c<0):
	print("Entrada:", a, ",", b, ",", c)
	print("Area:", mensagem)
else:
	print("Entrada:", a, ",", b, ",", c)
	print("Area:", area)
