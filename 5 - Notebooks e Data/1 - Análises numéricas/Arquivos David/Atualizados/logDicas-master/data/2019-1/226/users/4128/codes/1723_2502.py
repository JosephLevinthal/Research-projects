from math import*
h = int(input("insira um numero:"))

raiz = sqrt(12)
t = 0
c = 0

while(t < h):
	c = c +(-1) ** (t) * 1 /((2 * t + 1) * 3** t) * raiz 
	t = t + 1       #alcançar o valor de h
	
print(round(c, 8)) 
