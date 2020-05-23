m = int(input("Insira: "))
n = int(input("Insira: "))

i = 0
d = 0
soma = 0
while(i <= m/2):
	i = i + 1
	if((m%i) == 0):
		d = d + 1
		soma = soma + i
print(soma)
i2 = 0
d2 = 0
soma2 = 0
while(i2 <= n/2):
	i2 = i2 + 1
	if((n%i2) == 0):
		d2 = d2 + 1
		soma2 = soma2 + i2
print(soma2)
if((soma == n) and (soma2 == m)):
	print("AMIGOS")
else:
	print("NAO AMIGOS")