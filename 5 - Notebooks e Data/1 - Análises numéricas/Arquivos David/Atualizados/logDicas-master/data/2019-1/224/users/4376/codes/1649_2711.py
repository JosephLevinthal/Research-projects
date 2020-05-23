a=float(input("quanto vc em:     "))
b=int(input("quantos tickets vc quer comprar:   "))
c=float(input("valor dos tickets:    "))
d=int(input("quantidade de passes:   "))
e=float(input("valor dos passes:   "))
f=b*c+d*e
if(a>f):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
