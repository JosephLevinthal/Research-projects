x = int(input("digite os minutos do cliente: "))
if (x<=100):
	x1 = x* 1.2
	
else:
	x1 = x*1.4 + 25
print(round(x1,2))