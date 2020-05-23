escala =  input("qual a escala:")
vdatemperatura = int(input("valor da temperatura:"))

if (escala == "C"):
	F = (((9/5)* vdatemperatura)+ 32)
	print(round(F,2))
else:
	C= (5/9)*(vdatemperatura - 32)
	print(round(C,2))