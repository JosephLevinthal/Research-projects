x = int(input("Digite um numero inteiro: "))
y = 0
total = 0
while(y < x - 1):
	y = y + 1
	if(x % y == 0):
		print(y)
		total = total + y
if(total == x):
	print("PERFEITO")
else:
	print("NAO PERFEITO")

		