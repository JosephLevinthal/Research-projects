escala=input("escala")
temp=float(input("tempe"))
if(escala.upper()=="F"):
	w=5/9*(temp-32)
	print(w)
if(escala.upper()=="C"):
	h=((9*temp)/5) + 32
	print(h)
	