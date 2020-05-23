v = float(input("digite o valor disponivel: "))
r = int(input("quantidade de tickets do ru: "))
vt = float(input("digite o valor dos tickets: "))
ps = int(input("digite a quantidade de passes de onibus: "))
vp = float(input("digite o valor dos passes: "))

h = r * vt
g = ps * vp

x = h+g
if v >= x:
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")