x=float(input("Quantidade incial de pexe: "))
y=float(input("Percentual de cresicmneto: "))
h=0
while(x>0)and(x<8000):
	z=float(input("Pexe pra vender: "))
	x=x+(x*(y/100))
	x=x-z
	h=h+1
if(x<=0):
	print("ZERO")
	print(h)
else:
	print("MAXIMO")
	print(h)