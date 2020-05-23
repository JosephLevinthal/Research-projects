v= float(input("valor disponivel :"))
ru= int(input("tickets do ru :"))
vt= float(input("valor do ticket :"))
po= int(input("passes de onibus :"))
vp= float(input("valor dos passes de onibus :"))

vari= ru * vt + po * vp 

if (v >= vari) :
	print("SUFICIENTE")
	
else :
	print("INSUFICIENTE")
