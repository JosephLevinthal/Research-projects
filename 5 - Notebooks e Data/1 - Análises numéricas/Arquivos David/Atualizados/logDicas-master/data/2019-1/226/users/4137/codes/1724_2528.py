num = int(input("Digite um numero:"))
num1 = num
cont = 1
d = 10

while(num>9):
	num = num//10
	cont = cont + 1
	du = num//10
	d = d*10
	dig1 = num1//(d**(cont-1))
	print(dig1)