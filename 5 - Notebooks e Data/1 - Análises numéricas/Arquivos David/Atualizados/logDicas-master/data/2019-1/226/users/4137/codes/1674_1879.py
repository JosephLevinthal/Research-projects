# Ao testar sua solução, não se limite ao caso de exemplo.
n  = float(input("Numero de horas extras:"))
nf = float(input("Numero de horas faltadas:"))

h =round(n - ((1/4)*nf), 2)

if(h <= 400):
	print(n, "extras e", nf, "de falta")
	print("R$",100.0)
else:
	print(n, "extras e", nf, "de falta")
	print("R$",500.0)