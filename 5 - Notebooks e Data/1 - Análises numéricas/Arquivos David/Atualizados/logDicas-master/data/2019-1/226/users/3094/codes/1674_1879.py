# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input(''))
y=float(input(''))
z=x-((1/4)*y)
if(z>400):
	n=round(500.00,2)
else:
	n=round(100.00,2)
print(x, 'extras e', y, 'de falta')
print('R$', n)