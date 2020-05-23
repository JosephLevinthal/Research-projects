a= float(input("num a: "))
b= float(input("num b: "))
c= float(input("num c: "))
d= float(input("num d: "))

print("intervalo 1:", a , ",", b)
print("intervalo 2:", c, ",", d)

if (b<=a) or (d<=c):
	print("Entradas invalidas")
elif (b<c):
	print("Nao ha intersecao")
else:
	print("ha intersecao")
