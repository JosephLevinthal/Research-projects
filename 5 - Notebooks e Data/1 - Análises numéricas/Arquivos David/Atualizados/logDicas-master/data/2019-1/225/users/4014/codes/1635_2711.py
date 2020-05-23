x=float(input("valor:"))
y=int(input("quantidade de tickets do RU:"))
z=float(input("valor de tickets:"))
w=int(input("quantidade de passes de onibus:"))
a=float(input("valor dos passes:"))
b=(y*z)+(w*a)
if(x>b):
	msg="SUFICIENTE"
else:
	msg="INSUFICIENTE"
print(msg)