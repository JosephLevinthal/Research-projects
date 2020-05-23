a = float(input("altura da torre: "))
s = float(input("velocidade: "))
d = float(input("descida: "))
t = 0
h = 0
while h<a:
	h = h + s 
	if (h < a):
		h = h - d
	t = t + 1
print(t)