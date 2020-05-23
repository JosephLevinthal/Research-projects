from math import *

# leituira dos lados a,b,c
a = float(input("lado a:"))
b = float(input("lado b:"))
c = float(input("lado c:"))

print("Entradas:", a, ",", b, ",",c)

#testa se pelo menos uma das entrdas é negativa
if((a >0) or (b > 0) or (c > 0)):
	#testa se as medidas correwspidem a de um triangulo
	if((a < b + c) and (c < a + b) and ( b < c + a)):
		S = (a + b + c) / 2.0
		area = sqrt(S * (S - a) * (S - b) * (S - c))
		area = round(area,3)
		print("Area:" , area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
		