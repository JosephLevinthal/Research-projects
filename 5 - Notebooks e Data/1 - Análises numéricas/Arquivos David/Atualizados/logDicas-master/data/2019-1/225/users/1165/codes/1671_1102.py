from math import*
h = float(input("Altura total do tanque: "))
r = float(input("Raio dos bojos: "))
n = float(input("Nivel do combustivel: "))
 
if (n < 0 or h < 0 or r < 0):
	vol = -1
elif (n < r):
	vol = pi/3 * n**2 * (3 * r - n)
elif (n < h - r):
	vol = (4/3) * pi * r**3 + pi * r**2 * (n - r)
elif (n <= h):
	vol = (4/3) * pi * r**3 + pi * r**2 * (h - 2 * r) -  (4/3) * pi * (h -n)**2 * (3 * r - h + n)
else:
	vol = -1
print(round(vol, 3))