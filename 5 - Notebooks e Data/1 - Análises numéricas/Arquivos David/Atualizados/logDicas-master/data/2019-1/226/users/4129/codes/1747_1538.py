x = float(input("Numero x : "))
k = int(input("Numero de termos: "))

a = 0 #contadora
z = 2
s = 1
o = 1
b = 0
c = 1

h = 0

while (a < k):
	serie = 1 + h
	h = (x**z)*(-1)**s + h
	z = z + 2
	s = s + 1
	a = a + 1

print(round(serie, 8))
	