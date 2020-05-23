po=int(input("quantidade de pecas de ouro: "))
nome=input("nome da armadura: ")
d=int(input("fator de destreza: "))
nome= nome.upper()

fr1= 30 * d - 20
fr2= 15 * d - 1
fr3= 20 * d - 18

if( 1<=d<=8 and nome=="INTEIRA" and po>=200):
	print(fr1)
elif( 1<=d<=8 and nome=="PLACA" and po>=100):
	print(fr3)
elif( 1<=d<=8 and nome=="MALHA" and po>=50):
	print(fr2)
elif(po<50):
	print("PO insuficiente")
else:
	print("Entrada invalida")