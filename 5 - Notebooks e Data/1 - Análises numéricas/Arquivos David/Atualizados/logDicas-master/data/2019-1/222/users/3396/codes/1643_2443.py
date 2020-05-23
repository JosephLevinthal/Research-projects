from math import*
r=float(input("r:"))
a=float(input("a:"))
opcao=int(input("opcao:"))
if(opcao == 1):
	v= ((pi*(a**2)*(3*r-a))/3)
else:
	v=((4*pi*(r**3))/3)
print(round(v, 4))