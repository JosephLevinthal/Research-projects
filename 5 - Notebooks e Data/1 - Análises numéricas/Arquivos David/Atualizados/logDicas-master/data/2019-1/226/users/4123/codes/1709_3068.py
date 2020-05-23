n = input()
d = int(input())
v1 = int(input())
v2 = int(input())
V = -1
if v1>0 and v1<=10 and v2>0 and v2<=10:
	V = 2*(v1+v2) + 2*d if n == "CIMITARRA" else V
	V = 2*(v1+v2) + d if n == "KATANA" else V
	V = v1+v2 + 2*d if n == "SABRE" else V
if V < 0:
	print("Entrada invalida")
else:
	print(V)