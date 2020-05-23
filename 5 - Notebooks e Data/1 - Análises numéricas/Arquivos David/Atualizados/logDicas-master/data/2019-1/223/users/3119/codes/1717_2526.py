c = int(input("capacidade: "))
e = int(input("estoque: "))
q = int(input("quantidade"))

semana = 0
t = 0

while(e > 0):
	q = q * (semana + 1)
	e = (e - c) + q
	t = t + 1

print(t)
