from numpy import *
n = array(eval(input("Ve")))
i = 0
m = 0
while(i < size(n)):
	m = m + n[i]**(1/6)
x = m / size(n)
y = x ** (6)
print(round(y, 2))