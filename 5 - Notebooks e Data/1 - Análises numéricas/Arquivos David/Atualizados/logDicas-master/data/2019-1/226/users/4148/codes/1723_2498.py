a = int(input("hab1:"))
b = int(input("hab2: "))
p1=float(input("pA: "))
p2=float(input("pb: "))

Pa = p1/100
Pb = p2/100

ano = 0

while(a < b):
	a = a + (a * Pa)
	b = b + (b * Pb)
	ano = ano + 1
print(ano)
	