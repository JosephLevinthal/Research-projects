x=float(input("Quantidade incial de pexe: "))
y=float(input("Percentual de cresicmneto: "))
z=float(input("Peixe tirado por anos"))
h=0

while(x>0)and(x<12000):
	x=x+(x*(y/100))
	x=x-z
	h=h+1
if(x<=0):
	print("EXTINCAO")
	print(h)
else:
	print("LIMITE")
	print(h)