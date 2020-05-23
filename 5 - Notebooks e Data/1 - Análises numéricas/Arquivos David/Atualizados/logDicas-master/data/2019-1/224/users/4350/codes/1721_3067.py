x = input("ESPADA OU CAUDA")
a = int(input("D1"))
b = int(input("D2"))
c = int(input("D3"))
d = int(input("D4"))
if x == "ESPADA":
	t = a+6+b+6+c+6+d+6
elif x == "CAUDA":
	t = (a+b+c)*d
else:
	t = "Entrada invalida"
print(t)
	
