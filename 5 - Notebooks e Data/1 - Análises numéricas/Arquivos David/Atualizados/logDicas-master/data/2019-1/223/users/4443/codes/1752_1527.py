sf = int(input("Quantidade inicial de seguidores do deus Forseti: "))
sl = int(input("Quantidade inicial de seguidores do deus Loki: "))
pf = float(input("Percentual anual de crescimento seguidores Forseti: "))
pl = float(input("percentual anual de crescimento seguidores Loki:  "))

i = 0
sl = sl
sf = sf
while(sl < sf):
	sl = sl + (sl*pl/100)
	sf = sf + (sf*pf/100)
	i = i+1
print(i)	
