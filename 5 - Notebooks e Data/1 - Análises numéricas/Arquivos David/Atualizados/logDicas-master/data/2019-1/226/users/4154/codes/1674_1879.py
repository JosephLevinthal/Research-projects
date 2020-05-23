# Ao testar sua solução, não se limite ao caso de exemplo.
a = float(input('horas extras: '))
b = float(input('horas de falta: '))
h = round(a - (1/4)*b,2)
if h>400:
	print(a,'extras e',b,"de falta")
	print('R$',500.0)
else:
	print(a,'extras e',b,"de falta")
	print('R$',100.0)