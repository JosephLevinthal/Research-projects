p=float(input("valor:"))
e=int(input("quantidade de tickets do RU:"))
d=float(input("valor dos tickets:"))
r=int(input("quantidade de passes de ônibus:"))
o=float(input("valor dos passes:"))
l=(e*d)+(r*o)
if(p>l):
	m="SUFICIENTE"
else:
	m="INSUFICIENTE"
print(m)