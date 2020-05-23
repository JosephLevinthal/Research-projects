do1=float(input("distancia entre olhos:"))
dn1=float(input("diustancia entre o nariz e queixo: "))
do2=float(input("distancia entre olhos:"))
dn2=float(input("diustancia entre o nariz e queixo: "))
do3=float(input("distancia entre olhos:"))
dn3=float(input("diustancia entre o nariz e queixo: "))
f1=do1/dn1
f2=do2/dn2
f3=do3/dn3
x=f1-f2
y=f2-f3
w=f1-f3
if abs(x)<abs(y) and abs(x)<abs(w) :
	print("1 e 2")
elif abs(y)<abs(x) and abs(y)<abs(w):
	print("2 e 3")	
else:
	print("1 e 3")