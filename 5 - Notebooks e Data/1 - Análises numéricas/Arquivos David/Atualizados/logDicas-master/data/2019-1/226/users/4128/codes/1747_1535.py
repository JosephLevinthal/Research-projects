x = float(input("numero real:"))
k = int(input("termos da serie:"))

at = 0
sx = 1
t = 0
e = 2

while( t < k):
	at = ((x**sx) / sx) * (-1)**e +at
	t = t + 1
	e = e + 1
	sx = sx + 2
print(round(at,6))

v