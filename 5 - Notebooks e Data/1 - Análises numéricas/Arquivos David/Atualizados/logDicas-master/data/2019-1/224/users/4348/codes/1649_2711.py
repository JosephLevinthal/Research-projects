a=float(input("valor disponivel:"))
b=int(input("qtd de tickets do RU:"))
c=float(input("valor dos tickets:"))
d=int(input("qtd de passes do onibus:"))
e=float(input("valor dos passes:"))
eq=(b*c) + (d*e)
if(a>=eq):
	msg="suficiente".upper( )
else:
	msg="insuficiente".upper( )
print(msg)