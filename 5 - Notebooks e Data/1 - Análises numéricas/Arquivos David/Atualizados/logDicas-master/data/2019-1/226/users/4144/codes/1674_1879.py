# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input("horas extras: "))
b = float(input("horas que funcionario faltou: "))
h = (a) - ((1/4) * b)
print(a, "extras e", b, "de falta")
if(h>400):
	print("R$ 500.0")
else:
	print("R$ 100.0")