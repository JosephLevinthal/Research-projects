from math import*

r=float(input("Digite o raio do tanque: "))
x=float(input("Digite a altura da coluna de ar: "))
z=input("Digite um ou dois : ")
v=(pi*(x**2))*((3*r)-x)/3
y=((4*pi)*(r**3))/3
if(z=="1"):
	print(round(v,4))
else:
	print(round(y-v,4))
	
	
		  
		  
		  
		  