# Ao testar sua solução, não se limite ao caso de exemplo.
y=float(input("Valor de y: "))
x=float(input("Valor de x: "))
if((y>0)and(x>0)):
	print('Q1')
elif((y>0)and(x<0)):
	print('Q2')
elif((y<0)and(x<0)):
	print('Q3')
elif((y<0)and(x>0)):
	print('Q4')
elif((y!=0)and(x==0)):
	print('Eixo X')
elif((y==0)and(x!=0)):
	print('Eixo Y')
elif((y==0)and(x==0)):
	print('Origem')
else:
	print('Entrada invalida')