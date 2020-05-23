num = int(input("Informe um numero qualquer: \n"))
cont = 1
x = 0

while(cont<=num):
	if(num%cont==0):
		x = x + 1
		print(cont)
	cont = cont + 1
if(x==1):
	print("1 divisor")
else:
	print(x,"divisores")