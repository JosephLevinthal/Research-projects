from math import *
# Leitura das medidas tanque:
H = float(input("Digite a altura do tanque: "))
h = float(input("Digite a altura do combustivel no tanque: "))
r = float(input("raio dos bojos semiesfericos: "))

#Volume total da esfera => semiesfera inferiro e semiesfera superior:
Ve = ((4/3)*pi*(r**3))

#Volume da semiesfera:
se = (2/3*pi*(r**3))

if((H <= 0) or (h <=0) or (r <= 0) or (H <= h) or (H <= 2*r)):
	print("Entradas:", H,",", h,",", r)
	print("Entradas invalidas")

# Volume no corpo do cilindro
elif(h >= r):
	cil = (pi*(r**2)*(h-r)) + se 	
	vcil = 1000*cil
	print("Entradas:", H,",", h,",", r)
	print("Volume:", round(vcil, 3), "litros")

# Volume na semiesfera iferior
elif(h < r):
	si = pi/3*(h**2)*(3*r-h) 	
	vsi = 1000*si
	print("Entradas:", H,",", h,",", r)
	print("Volume:", round(vsi, 3), "litros")

# Volume na semiesfera superior	
elif(r > H - h):
	ss = (cil + 2*se)-si
	vss = 1000*ss
	print("Entradas:", H,",", h,",", r)
	print("Volume:", round(vss, 3), "litros")
	
