a=float(input("valor disponovel: "))
b=int(input("quantidade de tickets do RU: "))
c=float(input("valor dos tickets: "))
d=int(input("quantidade de passes de onibus:"))
e=float(input("valor dos passes: "))
s= a - (b*c+d*e)
if (s>=0):
	print("suficiente".upper())
else:
	print("insuficiente".upper())