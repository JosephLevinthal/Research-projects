a= float(input("Valor disponivel:"))
b= int(input("Quant de tickets:"))
c= float(input("Valor dos tickets:"))
d= int(input("Quant de passes:"))
e= float(input("Valor dos passes:"))

j= (b * c) + (d * e)
if (a >= j):
	msg= "SUFICIENTE"
else:
	msg= "INSUFICIENTE"
print(msg)