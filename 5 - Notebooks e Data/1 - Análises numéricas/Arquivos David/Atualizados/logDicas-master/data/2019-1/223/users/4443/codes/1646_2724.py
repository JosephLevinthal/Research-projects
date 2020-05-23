#Leitura dos numeros inteiros
a = int(input("digite um numero inteiro a: "))
b = int(input("digite um numero inteiro b: "))
c = int(input("digite um numero inteiro c: "))

maior = max(a, b, c)
#menor = min(a, b, c)
#meio = (a+b+c) - maior - menor

#Definicao do meio

meio = a

if (a>b) and (a<c) or (a>c) and (a<b):
	meio = a
else:
	if(a<b) and (b<c) or (b>c) and (a>b):
		meio = b
	else:
		meio = c

print(meio)

