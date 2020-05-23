jogos = int(input("1,2:"))
preco1 = float(input())
preco2 = float(input())
z = (((-preco2/4)+preco2)+preco1)
if (jogos == 1):
	a = preco1
if (jogos == 2):
	a = z
print(round(a,2))