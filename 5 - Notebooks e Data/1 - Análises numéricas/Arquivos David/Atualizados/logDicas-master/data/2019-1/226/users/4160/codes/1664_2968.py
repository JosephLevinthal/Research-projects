x = input("Digite se L ou S: ").upper()
a = float(input ("Digite a quantidade: "))
b = float(input("Digite a quantidade de refrigerante: "))
L = 5
S = 3.5
R = 4
if (x == "L"): 
	resp = (a * L) + (b * R)
	print(round(resp,2))
else:
	resp = (a * S) + (b * R)
	print(round(resp,2))