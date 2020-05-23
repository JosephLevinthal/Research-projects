from numpy import*

a=array(eval(input('peso: ')))
b=array(eval(input('altura: ')))
c=zeros(size(a))
for i in range(size(a)):
	c[i]=round((a[i])/((b[i])**2),2)
print(c)
d=max(c)
print('O MAIOR IMC DA TURMA EH:',d)
if(d<17):
	print('MUITO ABAIXO DO PESO')
if(d>=17 and d<=18.49):
	print('ABAIXO DO PESO')
if(d>=18.49 and d<=24.99):
	print('PESO NORMAL')
if(d>=25 and d<=29.99):
	print('ACIMA DO PESO')
if(d>=30 and d<=34.99):
	print('OBESIDADE')
if(d>=35 and d<=39.99):
	print('OBESIDADE SEVERA')
if(d>=40):
	print('OBESIDADE MORBIDA')