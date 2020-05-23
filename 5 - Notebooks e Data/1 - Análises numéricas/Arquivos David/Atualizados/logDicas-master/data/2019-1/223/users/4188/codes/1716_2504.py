v=int(input("Qt. virus: "))
l=int(input("leucocitos no sangue: "))
vp=int(input("porcentagem de virus:"))
lp=int(input("porcetagem de leuc.: "))
dia=0
while(l < v*2):
	v = v + (v*(vp/100))
	l = l + (l*(lp/100))
	dia = dia + 1
print(dia)