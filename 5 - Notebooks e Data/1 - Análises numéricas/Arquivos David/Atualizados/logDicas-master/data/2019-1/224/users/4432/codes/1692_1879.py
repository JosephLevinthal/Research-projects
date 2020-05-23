# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input("extrx  "))
b=float(input("falta  "))
h=(a)-(1/4*b)
print(round(a,2)," extras e ",round(b,2)," de falta")
if(h>400):
	print("R$ 500.0")
else:
	print("R$ 100.0")