from math import*
r = float(input("raio da circunferencia: "))
h = float(input("altura da coluna de ar: "))
n = int(input("digite um numero de (1/2):"))
volume_calota = pi * h**2 * (3*r - h)/3
volume_esfera = 4*pi*r**3 / 3
if (n == 1):
	msg = volume_calota
else:
	msg = volume_esfera - volume_calota
print(round(msg, 4))