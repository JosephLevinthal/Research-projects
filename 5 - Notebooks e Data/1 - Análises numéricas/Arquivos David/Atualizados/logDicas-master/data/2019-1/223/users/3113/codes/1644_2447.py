p1=float(input("preco:"))
p2=float(input("pagamento:"))
X= p1-p2
Y= p2-p1
p="Troco"+" "+"de"+" "
if(p1>p2):
	s=("Falta"+" "+str(X))
else:
	s=("Troco de"+" "+str(Y))
print(s)