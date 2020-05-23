#Entrada dos numeros inteiros positivos
n1 = int(input("Digite um numero inteiro positivo: "))
n2 = int(input("Digite outro numero inteiro positivo: "))

soma1 = 0 #variavel acumuladora do n1
soma2 = 0 #variavel acumuladora do n2
i1 = 0 #variavel contadora do n1
i2 = 0 #variavel contadora do n2

#montagem do laco de repeticao

while (i1 < n1-1):
	r1 = n1%(i1+1)
	if (r1 == 0):
		div1 = i1+1
		soma1 = soma1 + div1
	i1 = i1 + 1	
print(soma1)

while (i2 < n2-1):
	r2 = n2%(i2+1)
	if (r2 == 0):
		div2 = i2+1
		soma2 = soma2 + div2
	i2 = i2+1	
print(soma2)
if(soma1 == n2 and soma2 == n1):
	print("AMIGOS")
else:
	print("NAO AMIGOS")