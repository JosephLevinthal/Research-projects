var1 = input("(L/S: )")
var2 = int(input("Quantidade: "))
var3 = int(input("Quantidade de refrigerante: "))
l = 5.00
s = 3.50
r = 4.00

if(var1 == "L"):
	print(float(var2*l + var3*r))
else:
	print(float(var2*s + var3*r))