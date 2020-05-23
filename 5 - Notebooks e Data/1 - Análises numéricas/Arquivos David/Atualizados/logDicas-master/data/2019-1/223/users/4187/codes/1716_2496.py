#primeiro input
num1 = int(input("Digite um numero1:"))

soma = num1
total = 0
while (num1 != -1 ):
	num1 = int(input("Digite um numero12:"))
	soma = soma + num1
	total = num1 + soma
	if(num1 == -1):
		print(total + 1 + 1)
		
