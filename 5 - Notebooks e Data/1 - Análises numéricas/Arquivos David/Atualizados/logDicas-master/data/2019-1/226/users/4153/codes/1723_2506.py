# quantidade inicial de peixes
x = int(input("Insira: "))
# Percentual de crescimento anual do numero de peixes
y = int(input("Insira: "))
# Quantidade de tambaquis retirados por ano
z = int(input("Insira: "))
t = 0

while((x < 12000) and (x > 0)):
	q = x * (y/100)
	x = x + q - z
	t = t + 1

if(x > 12000):
	print("LIMITE")
else:
	print("EXTINCAO")
print(t)