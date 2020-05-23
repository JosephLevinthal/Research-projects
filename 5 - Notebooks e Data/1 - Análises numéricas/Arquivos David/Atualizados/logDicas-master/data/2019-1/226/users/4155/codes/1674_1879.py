x = float(input("quantidade de horas extras: "))
y = float(input("quantidade de horas que ele(a) faltou: "))
print(x, "extras", "e", y, "de falta")
	
H = x - (1/4 * y)
r = round(H, 2)

if(r > 400):
	print("R$", 500.0)
else:
	print("R$", 100.0)	
	