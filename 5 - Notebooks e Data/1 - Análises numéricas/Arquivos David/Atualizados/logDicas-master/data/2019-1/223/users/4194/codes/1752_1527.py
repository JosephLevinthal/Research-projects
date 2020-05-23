sf = int(input("Seguidores do deus Forseti: "))
sl = int(input("Seguidores do deus Loki: "))
pf = float(input("Percentual anual do deus Forseti: "))
pl = float(input("Percentual anual do deus Loki: "))

forse = 0
loki = 0
ano = 0
var1 = sf * pf
var2 = sl * pl

while(forse > loki):
	taxa = var1 - var2
	ano = ano + 1
	print(ano)