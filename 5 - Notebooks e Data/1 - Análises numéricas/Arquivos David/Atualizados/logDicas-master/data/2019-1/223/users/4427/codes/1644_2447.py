#Leia dois numeros reais
a=float(input("digite o preço da mercadoria: "))
b=float(input("digite o valor pago: "))

#calcule a diferenca
x = a-b
y = b-a

#condicao e impress
if (a>b):
	s=("Falta"+" "+str(x))
else:
	s=("Troco de"+" "+str(y))
print(s)