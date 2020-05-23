a = int(input("Digite um numero: "))	
b = int(input("Digite um numero: "))
ca = float(input("Digite um numero: "))
cb = float(input("Digite um numero: "))
f = ca/100
g = cb/100
ano = 0
while a <= b:
	c1 = a * f 
	a = a + c1
	c2 = b * g
	b = b + c2
	ano += 1
print(ano)