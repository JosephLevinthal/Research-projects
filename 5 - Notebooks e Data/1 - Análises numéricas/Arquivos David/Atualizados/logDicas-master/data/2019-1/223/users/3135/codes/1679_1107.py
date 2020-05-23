d= int(input("Insira o dia da semana (de 0 a 6):"))

f= int(input("Insira o dia do futuro:"))
c= f%7
if (d>6 or d<0):
	print("A entrada",d,"eh invalida")

elif(d==0 and c==0):
	print("Hoje eh domingo e o dia futuro eh domingo")
elif(d==0 and c==1):
	print("Hoje eh domingo e o dia futuro eh segunda")
elif(d==0 and c==2):
	print("Hoje eh domingo e o dia futuro eh terca")
elif(d==0 and c==3):
	print("Hoje eh domingo e o dia futuro eh quarta")
elif(d==0 and c==4):
	print("Hoje eh domingo e o dia futuro eh quinta")
elif(d==0 and c==5):
	print("Hoje eh domingo e o dia futuro eh sexta")
elif(d==0 and c==6):
	print("Hoje eh domingo e o dia futuro eh sabado")

elif(d==1 and c==6):
	print("Hoje eh segunda e o dia futuro eh domingo")
elif(d==1 and c==0):
	print("Hoje eh segunda e o dia futuro eh segunda")
elif(d==1 and c==1):
	print("Hoje eh segunda e o dia futuro eh terca")
elif(d==1 and c==2):
	print("Hoje eh segunda e o dia futuro eh quarta")
elif(d==1 and c==3):
	print("Hoje eh segunda e o dia futuro eh quinta")
elif(d==1 and c==4):
	print("Hoje eh segunda e o dia futuro eh sexta")
elif(d==1 and c==5):
	print("Hoje eh segunda e o dia futuro eh sabado")

elif(d==2 and c==5):
	print("Hoje eh terca e o dia futuro eh domingo")
elif(d==2 and c==6):
	print("Hoje eh terca e o dia futuro eh segunda")
elif(d==2 and c==0):
	print("Hoje eh terca e o dia futuro eh terca")
elif(d==2 and c==1):
	print("Hoje eh terca e o dia futuro eh quarta")
elif(d==2 and c==2):
	print("Hoje eh terca e o dia futuro eh quinta")
elif(d==2 and c==3):
	print("Hoje eh terca e o dia futuro eh sexta")
elif(d==2 and c==4):
	print("Hoje eh terca e o dia futuro eh sabado")

elif(d==3 and c==4):
	print("Hoje eh quarta e o dia futuro eh domingo")
elif(d==3 and c==5):
	print("Hoje eh quarta e o dia futuro eh segunda")
elif(d==3 and c==6):
	print("Hoje eh quarta e o dia futuro eh terca")
elif(d==3 and c==0):
	print("Hoje eh quarta e o dia futuro eh quarta")
elif(d==3 and c==1):
	print("Hoje eh quarta e o dia futuro eh quinta")
elif(d==3 and c==2):
	print("Hoje eh quarta e o dia futuro eh sexta")
elif(d==3 and c==3):
	print("Hoje eh quarta e o dia futuro eh sabado")

elif(d==4 and c==3):
	print("Hoje eh quinta e o dia futuro eh domingo")
elif(d==4 and c==4):
	print("Hoje eh quinta e o dia futuro eh segunda")
elif(d==4 and c==5):
	print("Hoje eh quinta e o dia futuro eh terca")
elif(d==4 and c==6):
	print("Hoje eh quinta e o dia futuro eh quarta")
elif(d==4 and c==0):
	print("Hoje eh quinta e o dia futuro eh quinta")
elif(d==4 and c==1):
	print("Hoje eh quinta e o dia futuro eh sexta")
elif(d==4 and c==2):
	print("Hoje eh quinta e o dia futuro eh sabado")

elif(d==5 and c==2):
	print("Hoje eh sexta e o dia futuro eh domingo")
elif(d==5 and c==3):
	print("Hoje eh sexta e o dia futuro eh segunda")
elif(d==5 and c==4):
	print("Hoje eh sexta e o dia futuro eh terca")
elif(d==5 and c==5):
	print("Hoje eh sexta e o dia futuro eh quarta")
elif(d==5 and c==6):
	print("Hoje eh sexta e o dia futuro eh quinta")
elif(d==5 and c==0):
	print("Hoje eh sexta e o dia futuro eh sexta")
elif(d==5 and c==1):
	print("Hoje eh sexta e o dia futuro eh sabado")

elif(d==6 and c==1):
	print("Hoje eh sabado e o dia futuro eh domingo")
elif(d==6 and c==2):
	print("Hoje eh sabado e o dia futuro eh segunda")
elif(d==6 and c==3):
	print("Hoje eh sabado e o dia futuro eh terca")
elif(d==6 and c==4):
	print("Hoje eh sabado e o dia futuro eh quarta")
elif(d==6 and c==5):
	print("Hoje eh sabado e o dia futuro eh quinta")
elif(d==6 and c==6):
	print("Hoje eh sabado e o dia futuro eh sexta")
elif(d==6 and c==0):
	print("Hoje eh sabado e o dia futuro eh sabado")