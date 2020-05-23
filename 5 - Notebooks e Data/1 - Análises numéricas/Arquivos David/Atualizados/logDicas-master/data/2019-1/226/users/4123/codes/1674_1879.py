# Ao testar sua solução, não se limite ao caso de exemplo.
extra = float(input())
falta = float(input())
H = extra - 0.25*falta
print(extra," extras e ",falta," de falta")
if H>400:
	print("R$ 500.0")
else:
	print("R$ 100.0")