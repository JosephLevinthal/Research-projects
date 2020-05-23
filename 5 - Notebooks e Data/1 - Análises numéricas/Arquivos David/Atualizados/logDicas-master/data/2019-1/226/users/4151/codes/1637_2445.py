e=input("escala: (C/F) ")
t=float(input("valor da temperatura: "))
celsius=(5/9)*(t-32)
fa= (t * (9/5))+32

if(e.upper()=="F"):
	print(round(celsius,2))
else:
	print(round(fa,2))