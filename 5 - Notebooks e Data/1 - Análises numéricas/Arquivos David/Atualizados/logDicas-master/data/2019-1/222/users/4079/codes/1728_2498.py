a=int(input("n habitantes da cidade a1: "))
b=int(input("n habitantes da cidade b1: "))
c=float(input("crescimento populacional a2:"))
d=float(input("crescimento populacional b2:"))
ano=0

while(a < b):
	ano = ano+1
	a = a+a*c/100
	b=b+b*d/100
print(ano)