a=float(input("numero a :"))
b=float(input("numero b :"))
c=float(input("numero c :"))
d=float(input("numero d :"))
e=float(input("numero e :"))
f=float(input("numero f :"))



vari= (a * e - b * d)

if (vari != 0) :
	x = ((c * e) - (b * f)) / (vari)
	y = ((a * f) - (c * d)) / (vari)
	print(x)
	print(y)
	
else :
	
	print("Nao tem solucao")