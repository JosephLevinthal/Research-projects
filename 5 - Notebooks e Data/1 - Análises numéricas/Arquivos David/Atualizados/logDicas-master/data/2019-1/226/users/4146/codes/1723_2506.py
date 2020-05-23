p = int(input("Peixes: "))
c = int(input("Crescimento: "))
r = int(input("Retirados: "))
t = 0
crescp = p

while (crescp < 12000) and (crescp > 0):
	crescp = crescp + (crescp * (c/100)) - r
	t = t + 1
	
if (crescp <= 0):
	print("EXTINCAO")
else:
	print("LIMITE")
	
print(t)
		