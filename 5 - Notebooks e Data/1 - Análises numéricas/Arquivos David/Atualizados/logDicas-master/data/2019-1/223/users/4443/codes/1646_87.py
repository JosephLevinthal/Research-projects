#Leitura dos numeros inteiros
a = int(input("digite um numero inteiro a: "))
b = int(input("digite um numero inteiro b: "))
c = int(input("digite um numero inteiro c: "))

menor = a
if (a < b) and (a < c):
	menor =a
else:
	if (b < a) and (b < c):
		menor = b
	else:
		if (c < a) and (c < b):
			menor = c

print(menor)			
