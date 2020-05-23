a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))
x = (c * e) - (b * f)
y = (a * f) - (c * d)
var = (a * e) - (b * d)
if (var == 0):
	print("Nao tem solucao")
else:
	msg1 = x / var
	print(msg1)
	msg2 = y / var
	print(msg2)
	

	