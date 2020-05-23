h = float(input("horas extras"))
f = float(input("faltadas"))
print(h, "extras e", f, "de falta")
a = (h-(1/4)*f)
if a>400:
	t = 500.0
elif a<=400:
	t = 100.0
print("R$", t)