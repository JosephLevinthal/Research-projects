n = input("nome da arma:")
D = int(input("destreza do personagem:"))
d1 = int(input("dado 1:"))
d2 = int(input("dado 2:"))
s = d1 + d2
if ((n == "CIMITARRA") and (d1 >=1) and (d1 <=10) and (d2 >=1) and (d2 <= 10) and (D >0)):
	d = 2 * s + 2 * D
	print(d)
elif((n == "KATANA") and (d1 >=1) and (d1 <=10) and (d2 >=1) and (d2 <=10) and (D >0)):
	d = 2 * s + D
	print(d)
elif((n == "SABRE") and (d1 >=1) and (d1 <=10) and (d2 >=1) and (d2 <=10) and (D >0)):
   d = s + 2*D
   print(d)
else:
	print("entrada invalida")