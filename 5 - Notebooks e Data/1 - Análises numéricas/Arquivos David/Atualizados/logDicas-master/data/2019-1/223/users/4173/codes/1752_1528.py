dano = float(input())
troll = float(input())
rec = float(input())
rodadas = 0
while troll > 0:
	troll = troll - dano*5
	troll = troll + rec
	rodadas += 1
print(rodadas)