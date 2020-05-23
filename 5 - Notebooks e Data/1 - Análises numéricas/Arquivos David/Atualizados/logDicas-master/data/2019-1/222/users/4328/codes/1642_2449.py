# SISTEMA DE EQUAÇÕES DE DUAS VARIÁVEIS
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if ((a*e) - (b*d) != 0):
	print((c*e - b*f) / (a*e - b*d))
	print((a*f - c*d) / (a*e - b*d))
else:
	print(("Nao tem solucao"))
