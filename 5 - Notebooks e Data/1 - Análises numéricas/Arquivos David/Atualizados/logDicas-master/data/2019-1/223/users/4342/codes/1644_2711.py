a=float(input("valor:"))
b=float(input("quantidade de tickets do RU:"))
c=float(input("valor dos tickets:"))
d=float(input("quantidade de passes de onibus:"))
e=float(input("valor dos passes:"))
if (a > (b*c)+(d*e)):
	mensagem="SUFICIENTE"
else:
	mensagem="INSUFICIENTE"
print(mensagem)