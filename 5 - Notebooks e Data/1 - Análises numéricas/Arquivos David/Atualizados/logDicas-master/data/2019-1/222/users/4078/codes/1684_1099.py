# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de iden
a =float(input("lado1: "))
b =float(input("lado2: "))
c =float(input("lado3: "))
print("Entrada: ",a, ",",b, ",",c)
if(a < 0) or (b < 0) or (c < 0):
	tipo = "invalido"
elif(a >= b + c) or (b >= a + c) or (c >= a + b):
	tipo = "invalido"
else:
	if(a==b) and (b==c):
	    tipo = "equilatero"
	else:
		if((a==b) or (b==c) or (b==c)):
			  tipo = "isosceles"
		else:
			  tipo = "escaleno"
print("Tipo de triangulo",tipo)