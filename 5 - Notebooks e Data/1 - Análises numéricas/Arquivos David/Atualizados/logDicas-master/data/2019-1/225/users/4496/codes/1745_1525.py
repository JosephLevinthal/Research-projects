vi = int(input("Valor incial: "))
b = int(input("Bombeada: "))
r = int(input("Retirada: "))

v = 0
e = 0
t = 1

while(v > 1000):
	v = v + (vi + b) / r

	e = e + 1
	t = t + 2

print(t)