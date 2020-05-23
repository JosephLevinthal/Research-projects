do1 = float(input("distancia A1:"))
dn1 = float(input("distacia B1:"))
do2 = float(input("distancia A2:"))
dn2 = float(input("distancia B2:"))
do3 = float(input("distancia A3:"))
dn3 = float(input("distancia B3:"))

f1 = do1/dn1
f2 = do2/dn2
f3 = do3/dn3

if abs(f1-f2)<abs(f2-f3) and abs(f1-f2)<abs(f3-f1):
	print("1 e 2")
elif abs(f2-f3)<abs(f1-f2) and abs(f2-f3)<abs(f1-f3):
	print("2 e 3")
elif abs(f1-f3)<abs(f2-f3) and abs(f1-f3)<abs(f1-f2):
	print("1 e 3")
