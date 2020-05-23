from math import*
H=float(input("Digite a altura total do tanque: "))
h=float(input("Digite o nivel de combustivel no tanque: "))
r=float(input("Digite o raio dos bojos semiesfericos inferior e superior: "))
print("Entradas:",H,",",h,",",r)
a=(pi/3)*h**2*(3*r-h)
b=((2/3*pi*(r**3))+(pi*(r**2)*(h-r)))*1000
c=((4/3*(pi*(r**3)))+(pi*(r**2)*(H-2*r))-(1/3)*pi*(H-h)**2*(3*r-H+h))*1000
if((H<0)or(h<0)or(r<0))or((H<h)or(H<(2*r))):
	print("Entradas invalidas")
elif(h<=r):
		a=a*1000
		print("Volume:",(round(a,3)),"litros")
elif(h<H-r):
		 print("Volume:",(round(b,3)),"litros")
elif(h<=H):
       print("Volume:",(round(c,3)),"litros")		


		


