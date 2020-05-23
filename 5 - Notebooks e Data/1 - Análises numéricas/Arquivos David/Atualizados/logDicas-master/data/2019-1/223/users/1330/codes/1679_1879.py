# Ao testar sua solução, não se limite ao caso de exemplo.
nhe = float(input())
nhf = float(input())

v = (nhe - 1/4 * nhf)

if(v>400):
	print(nhe, " extras e", nhf, "de falta")
	print("R$", round(500.00,2))
else:
	print(nhe, " extras e", nhf, "de falta")
	print("R$", round(100.00,2))