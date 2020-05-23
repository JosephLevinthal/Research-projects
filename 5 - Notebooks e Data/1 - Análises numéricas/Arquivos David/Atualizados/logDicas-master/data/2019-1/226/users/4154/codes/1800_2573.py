from numpy import *
a = array(eval(input()))
b = array(eval(input()))
c = zeros(size(a))
d = 0
for i in range(size(a)):
	c[d] = round(a[d]/((b[d])**2),2)
	d += 1
print(c)
e = max(c)
print('O MAIOR IMC DA TURMA EH:',e)
if e < 17:
	print('muito abaixo do peso')
elif e >= 17 and e<=18.49:
	print('abaixo do peso')
elif e>= 18.50 and e<= 24.99:
	print('peso normal')
elif e >= 25 and <= 29.99:
	print('acima do peso')
elif e >= 25 and <= 29.99:
	print('acima do peso')
elif e >= 35 and <= 39.99:
	print('obesidade severa')