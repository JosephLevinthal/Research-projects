p = float(input("Digite o percurso em 'km': "))
t = str(input("Digite A ou B: "))
L = 1
A = 8 / L
B = 12 / L
c1 = p / A
c2 = p / B
if(t == "A"):
	print(round(c1, 2))
else:
	print(round(c2, 2))
	
