from math import*
n = int(input("Insira um numero: "))

x = 0
i = 0
c = 1


while(i < n):
	x = x + (-1)**(i) / (c * (3**i) )
	num = sqrt(12) * x 
	i = i + 1
	c = c + 2
	
print(round(num, 8))