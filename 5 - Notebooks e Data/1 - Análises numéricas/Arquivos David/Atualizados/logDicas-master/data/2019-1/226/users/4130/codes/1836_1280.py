from numpy import*
tabuleiro = array(eval(input("tabuleiro: ")))
mov = input("movimentos: ")
xtab = int(0)
ytab = int(0)
moeda = 0
life = 100
a = shape(tabuleiro)[1] - 1
b = shape(tabuleiro)[0] - 1
for x in mov:
	
	if x == "A":
		xtab = xtab - 1
		if xtab<0:
			xtab = xtab + 1
		if tabuleiro[ytab,xtab] ==33:
			xtab = xtab + 1
			
			
	elif x == "D":
		xtab = xtab + 1
		if xtab>a:
			xtab = xtab - 1
		if tabuleiro[ytab,xtab] ==33:
			xtab= xtab - 1
			
			
	elif x == "W":
		ytab =ytab - 1
		if ytab<0:
			ytab = ytab + 1
		if tabuleiro[ytab,xtab] ==33:
			ytab = ytab + 1
			
			
	elif x == "S":
		ytab= ytab + 1
		if ytab>b:
			ytab=ytab - 1
		if tabuleiro[ytab,xtab] ==33:
			ytab = ytab - 1
			
			
	if tabuleiro[ytab,xtab] ==11:
		moeda = moeda + 1
		tabuleiro[ytab,xtab] = 0
	elif tabuleiro[ytab,xtab] == 22:
		life = life - 5
	
	
		
print("posicao x: ",xtab)
print("posicao y: ",ytab)
print("moedas: ", moeda)
print("life: ", life)