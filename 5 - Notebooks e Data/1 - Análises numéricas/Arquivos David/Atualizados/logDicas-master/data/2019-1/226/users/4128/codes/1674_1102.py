from math import*

H = float(input("altura:"))
h = float(input("nivel de combustivel:"))
r = float(input("raio: "))

print("Entradas:", H,",", h,",", r)

Vc = pi*r**2*H #volume do cilindro	
Ve = (4/3)*pi*r**3 #volume da esfera
Va = (pi/3)*H**2*(3*r - H) #volume da calota

if((H == 0) or (h == 0) or (r == 0) or (H < h) or (H < 2*r)):
	print("Entradas invalidas")
elif(h < Ve) and (h > Va):
	V = Vc
	V = round(V,3)
	print( V ,"litros")

print(round(Vc,3))
print(round(Ve,3))
print(round(Va,3))
	
	