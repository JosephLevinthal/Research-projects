from math import*
r = float(input("Raio:"))
alt = float(input("Altura:"))
op = input("Opcao:")
volume = (4*pi*(r**3))/3
volcalota = (pi*(alt**2)*(3*r-alt))/3
combustive = volume - volcalota
if(op == "1"):
	print(round(volcalota, 4))
if(op=="2"):
	print(round(combustive, 4))