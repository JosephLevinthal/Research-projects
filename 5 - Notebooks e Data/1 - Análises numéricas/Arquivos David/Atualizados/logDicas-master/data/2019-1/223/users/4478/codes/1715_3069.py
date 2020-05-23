x = input("Ataque: ").upper() #ATAQUES: FURIA/GRITO/TOQUE
a = int(input("sorteio 1: "))
b = int(input("sorteio 2: "))

if((x=="FURIA")and(a>=1)or(a<=8)and(b>=1)or(b<=8)):
	pontos=(10+a+b)
	print(pontos)
elif((x=="GRITO")and(a>=1)and(a<=8)and(b>=1)and(b<=8)):
	pontos=(6+a+b)
	print(pontos)
elif((x=="TOQUE")and(a>=1)or(a<=8)and(b>=1)or(b<=8)):
	pontos=(a+b)**2
	print(pontos)
else:
	pontos="Entrada invalida"
	print(pontos)
