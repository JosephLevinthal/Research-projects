a= float(input("Num a: "))
b= float(input("Num b: "))
c= float(input("Num c: "))
d= float(input("Num d: "))
print("Intervalo 1: ", a, ",", b)
print("Intervalo 2:", c, ",", d)

if(b<=a) or (d<=c):
	print("Entradas invalidas")
elif(b+c):
	print("Nao ha intersecao")
else:
	print("Ha intersecao")
