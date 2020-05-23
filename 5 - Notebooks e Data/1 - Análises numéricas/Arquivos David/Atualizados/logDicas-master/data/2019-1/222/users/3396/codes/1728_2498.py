
a=int(input("numero de habitante a:"))
b=int(input("numero de habitante b:"))
c=float(input("percentual de a:"))
d=float(input("percentual de b:"))

ano=0
while	(a<b):
	ano=ano+1
	a=a+a*c/100
	b=b+b*d/100
print(ano)