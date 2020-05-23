qs = int(input("quantidade de suco"))
sal = int(input("quantidade de salgados"))
v = float(input("valor disponivel"))

vt = (qs * 3) + (sal * 3.50)
if v >= vt:
	m = "Sim"
else:
	m = "Nao"
print(round(vt, 2))
print(m)
													
