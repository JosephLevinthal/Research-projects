a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))
x = "Tipo de triangulo: "
y = "Entradas: "
e = "equilatero"
f = "isosceles"
g = "escaleno"
h = "invalido"
ent = a,b,c
print(y,a,",",b,",",c)
if  (a >= b + c) or (b >= a + c) or (c >= a + b):
	print(x + h)
elif a == b and b == c:
	print(x + e)
elif a == b or b == c or a == c:
	print(x + f)
else:
	print(x + g)
