n = int(input("Insira um numero: "))
y = 0
i = 0
c = 1


while(i < n):
	y = y + (-1)**i * 4 / c 
	i = i + 1
	c = c + 2
	
		
print(round(y, 8))