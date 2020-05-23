p = int(input("Peixes: "))
c = int(input("Crescimento: "))
crescp = p
t = 0

while (crescp < 8000) and (crescp > 0):
	r = int(input("Retirados: "))
	crescp = crescp + (crescp * (c/100)) - r
	t = t + 1
	
if (crescp <= 0):
	print("ZERO")
else:
	print("MAXIMO")
	
print(t)	