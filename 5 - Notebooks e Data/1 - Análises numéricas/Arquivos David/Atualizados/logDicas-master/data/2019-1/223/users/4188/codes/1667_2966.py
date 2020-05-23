n=input("promocao: ")
m=float(input("preco ingresso: "))
t=int(input("quantidade: "))
if (n.upper()=="S"):
	p=m*(80/100)*t
	print(round(p,2))
if (n.upper()=="N"):
	p=m*t
	print(round(p,2))
	