hf = float(input("Digite a altura total da Torre da Lua (em metros): "))
ms = float(input("Digite a distancia que Equecrates sobe por minuto: "))
md = float(input("Digite a distancia que Equecrates desce por minuto: "))

t = 0
he = 0
while(he < hf):
	he = (he + ms)
	if (he < hf):
		he = he - md
	t = t+1	
print(t)	
