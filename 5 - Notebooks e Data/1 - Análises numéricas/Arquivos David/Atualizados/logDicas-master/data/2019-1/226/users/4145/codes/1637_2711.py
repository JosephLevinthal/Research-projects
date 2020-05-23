v = float(input("valor disponivel: "))
qt = int(input("quantidade de tickets do ru: "))
pt = float(input("valor do ticket: "))
vt = int(input("quantidade de vales transporte: "))
pv = float(input("preco do vale transporte: "))

gasto = v - qt*pt - vt*pv
if (gasto >= 0):
	men = "SUFICIENTE"
else:
	men = "INSUFICIENTE"
	
print(men)	