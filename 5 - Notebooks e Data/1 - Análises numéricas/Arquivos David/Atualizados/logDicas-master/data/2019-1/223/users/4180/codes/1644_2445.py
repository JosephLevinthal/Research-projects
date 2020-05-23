escala=input("qual escala: ")
valordatemperatura=float(input("valor da temperatura: "))
if(escala=="C"):
	F=(((9/5)*valordatemperatura)+32)
	print(round(F,2))
else:
	C=(5/9)*(valordatemperatura-32)
	print(round(C,2))
