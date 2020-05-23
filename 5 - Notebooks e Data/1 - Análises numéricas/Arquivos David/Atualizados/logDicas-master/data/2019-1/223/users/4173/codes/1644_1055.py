from math import*
v = float(input())
a = radians(float(input()))
d = float(input())
g = 9.8
r = ((v**2)*sin(2*a))/g
if (r+0.1 >= d):
	  mensagem = "sim"
else:
	  mensagem = "nao"
print(mensagem)