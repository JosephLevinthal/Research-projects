# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input('Insira o numero de horas extras: '))
f = float(input('Insira o numero de horas faltas: '))
print(e,'extras e', f,'de falta')
h = e-1/4*f

if (h>400):
	print('R$ 500.0')
else:
	print('R$ 100.0')