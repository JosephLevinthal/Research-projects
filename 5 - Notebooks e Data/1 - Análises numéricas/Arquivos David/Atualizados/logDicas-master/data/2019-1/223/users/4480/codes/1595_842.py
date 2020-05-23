num = int(input("digite um numero inteiro: "))
soma = 0
while (num !=0):
	resto = num % 10
	num = (num - resto)//10
	soma = soma + resto
print(soma)