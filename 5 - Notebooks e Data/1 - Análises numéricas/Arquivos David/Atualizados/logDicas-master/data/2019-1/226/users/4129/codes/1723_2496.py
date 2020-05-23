num = int(input("Numero :"))

z = 0
while(num != -1):
	z = num + z
	num = int(input("Numero :"))
else:
	print(z)