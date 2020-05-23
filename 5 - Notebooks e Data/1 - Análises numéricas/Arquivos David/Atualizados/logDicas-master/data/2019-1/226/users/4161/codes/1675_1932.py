do1 = float(input("distancia entre os olhos imagem 1: "))
dnq1 = float(input("distancia entre nariz e queixo imagem 1: "))
do2 = float(input("distancia entre os olhos imagem 2: "))
dnq2 = float(input("distancia entre nariz e queixo imagem 2: "))
do3 = float(input("distancia entre os olhos imagem 3: "))
dnq3 = float(input("distancia entre nariz e queixo imagem 3: "))
p1 = do1/dnq1
p2 = do2/dnq2
p3 = do3/dnq3
c1 = abs(p1-p2)
c2 = abs(p2-p3)
c3 = abs(p1-p3)
v = min(c1,c2,c3)
if v==c1:
	print("1 e 2")
elif v==c2:
	print("2 e 3")
elif v==c3:
	print("1 e 3")