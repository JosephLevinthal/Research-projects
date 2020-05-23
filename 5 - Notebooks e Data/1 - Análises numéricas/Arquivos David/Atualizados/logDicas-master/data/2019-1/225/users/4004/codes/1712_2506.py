i = int(input("Quantidade inicial: "))          #Quantidade de peixes inicial
p = float(input("Percentual de crescimento: ")) #Percentual de crescimento
q = int(input("Quantidade vendida: "))          #Quantidade vendida anualmente

a = 0       #contador
t = i       #tambaqui
lim = 12000
p = p / 100 #percentual

while t > 0 and t < lim:
	t = t + ((t * p) - q)
	a = a + 1
if t <= 0:
	print("EXTINCAO")
elif t >= lim:
	print("LIMITE")
print(a)