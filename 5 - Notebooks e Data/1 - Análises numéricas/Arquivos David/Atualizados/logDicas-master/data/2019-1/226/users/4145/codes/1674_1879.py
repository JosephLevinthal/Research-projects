# Ao testar sua solução, não se limite ao caso de exemplo.
he = float(input("horas extras: "))
hf = float(input("horas nao trabalhadas: "))
h = he -1/4*hf
print(he," extras e", hf," de falta")
if(h>400):
	print("R$ ",500.0 )
else:
	print("R$ ",100.0)