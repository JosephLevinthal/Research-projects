from math import *

x = float(input("Digite o valor de x: "))
k = int(input("Digite o valor de k: "))

i = 0
y = 0

while (i < k):
	y = y + (x**(2*i+1)) / (factorial(2*i+1))
	i = i + 1
print(round(y, 9))
