nA=int(input("numero de habitantes da cidade A :"))
nB=int(input("numero de habitantes da cidade B :"))
cpA=float(input("crescimento populacional da cidade A :"))
cpB=float(input("crescimento populacional da cidade B :"))
t=0
xa= nA
xb=nB
while (xa <= xb) and (cpA > cpB) :
	xa=xa + (xa * (cpA / 100))
	xb=xb + (xb * (cpB / 100))
	t= t + 1 
print(t)