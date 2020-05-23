from numpy import *

x = array(eval(input()))
y = array(eval(input()))


a = zeros(size(x))

for i in range(size(x)):
	a[i] = round(x[i]/(y[i]*y[i]),2)
	
c = ""
n = max(a)

for i in range(size(a)):
	if n < 17:
		c = "muito abaixo do peso"
	if 17 <= n <= 18.49:
		c = "abaixo do peso"
	if 18.5 <= n <= 24.99:
		c= "peso normal"
	if 25 <= n <= 29.99:
		c= "acima do peso"
	if 30 <= n <=34.99:
		c = "obesidade"
	if 35 <= n <= 39.99:
		c= "obesidade severa"
	if n > 40:
		c = "obesidade morbida"
print(a)
print("O MAIOR IMC DA TURMA EH: ",n)
print(c.upper())