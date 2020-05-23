v = int(input("Quantidade de virus: "))
l = int(input("Quantidade de leucocitos: "))
pv = int(input("Crescimento de virus: "))
pl = int(input("Crescimento de leucocitos: "))
t = 0
crescv = v
crescl = l

while (crescv > crescl / 2):
	crescv = crescv + (crescv * (pv/100))
	crescl = crescl + (crescl * (pl/100))
	t = t + 1
	
print(t)	