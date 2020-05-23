a = int(input("qual o valor total : "))
b = int(input("quantos tickets: "))
c = float(input("qual o valor total dos tickets: "))
d = int(input("qual o total do passes"))
e = float(input("qual o valor dos passes: "))
c*b+e*d<=a
c*b+e*d>a
if (c*b+e*d<=a):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
print(mensagem)