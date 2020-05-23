#Leitura dos numeros inteiros
a = int(input("digite um numero inteiro a: "))
b = int(input("digite um numero inteiro b: "))
c = int(input("digite um numero inteiro c: "))

#print(max(a, b, c))

maior = a
if (a > b) and (a > c):
	maior = a
else:
	if (b > a) and (b > c):
		maior = b
	else:
		if (c > a) and (c > b):
			maior = c

print(maior)			
