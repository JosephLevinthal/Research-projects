qic = int(input("qtd de virus: "))
qil = int(input("qtd de leucocitos: "))
per1 = float(input("virus: "))
per2 = float(input("leuco: "))

v = qil #acumuladora de virus
l = qic #acumuladora de leucocitos
c = 0 #dias corridos

while(v < 2 * l):
	v = v + ((v * per2) / 100)
	l = l + ((l * per1) / 100)
	c = c + 1

print(c)
	