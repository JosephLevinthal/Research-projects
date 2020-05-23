Vi = int(input("Volume inicial: "))
Vb = int(input("Volume bombeado para dentro: "))
Vr = int(input("Volume retirado: "))

V = Vi     #Volume em tempo real
c = 0      #contador (em minutos)
lim = 1000 #limite para desativar o mecanismo

while V > lim :
	c = c + 1
	V = V + (Vb - Vr)
print(c)