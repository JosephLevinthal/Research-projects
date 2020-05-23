# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = int(input("escreva o numero correspondente ao dia de hoje: "))
b = int(input("escreva o numero de dias apos hoje: "))
c = (b % 7)

if ((a > 6) or (a < 0)):
	print ("A entrada", a, "eh invalida")
elif (a == 0) and (c == 0):
	print ("Hoje eh domingo e o dia futuro eh domingo")
elif (a == 0) and (c == 1):
	print ("Hoje eh domingo e o dia futuro eh segunda")
elif (a == 0) and (c == 2):
	print ("Hoje eh domingo e o dia futuro eh terca")
elif (a == 0) and (c == 3):
	print ("Hoje eh domingo e o dia futuro eh quarta")
elif (a == 0) and (c == 4):
	print ("Hoje eh domingo e o dia futuro eh quinta")
elif (a == 0) and (c == 5):
	print ("Hoje eh domingo e o dia futuro eh sexta")
elif (a == 0) and (c == 6):
	print ("Hoje eh domingo e o dia futuro eh sabado")
elif (a == 1) and (c == 0):
	print ("Hoje eh segunda e o dia futuro eh segunda")
elif (a == 1) and (c == 1):
	print ("Hoje eh segunda e o dia futuro eh terca")
elif (a == 1) and (c == 2):
	print ("Hoje eh segunda e o dia futuro eh quarta")
elif (a == 1) and (c == 3):
	print ("Hoje eh segunda e o dia futuro eh quinta")
elif (a == 1) and (c == 4):
	print ("Hoje eh segunda e o dia futuro eh sexta")
elif (a == 1) and (c == 5):
	print ("Hoje eh segunda e o dia futuro eh sabado")
elif (a == 1) and (c == 6):
	print ("Hoje eh segunda e o dia futuro eh domingo")
elif (a == 2) and (c == 0):
	print ("Hoje eh terca e o dia futuro eh terca")
elif (a == 2) and (c == 1):
	print ("Hoje eh terca e o dia futuro eh quarta")
elif (a == 2) and (c == 2):
	print ("Hoje eh terca e o dia futuro eh quinta")
elif (a == 2) and (c == 3):
	print ("Hoje eh terca e o dia futuro eh sexta")
elif (a == 2) and (c == 4):
	print ("Hoje eh terca e o dia futuro eh sabado ")
elif (a == 2) and (c == 5):
	print ("Hoje eh terca e o dia futuro eh domingo")
elif (a == 2) and (c == 6):
	print ("Hoje eh terca e o dia futuro eh segunda")
elif (a == 3) and (c == 0):
	print ("Hoje eh quarta e o dia futuro eh quarta")
elif (a == 3) and (c == 1):
	print ("Hoje eh quarta e o dia futuro eh quinta")
elif (a == 3) and (c == 2):
	print ("Hoje eh quarta e o dia futuro eh sexta")
elif (a == 3) and (c == 3):
	print ("Hoje eh quarta e o dia futuro eh sabado")
elif (a == 3) and (c == 4):
	print ("Hoje eh quarta e o dia futuro eh domingo")
elif (a == 3) and (c == 5):
	print ("Hoje eh quarta e o dia futuro eh segunda")
elif (a == 3) and (c == 6):
	print ("Hoje eh quarta e o dia futuro eh terca")
elif (a == 4) and (c == 0):
	print ("Hoje eh quinta e o dia futuro eh quinta")
elif (a == 4) and (c == 1):
	print ("Hoje eh quinta e o dia futuro eh sexta")
elif (a == 4) and (c == 2):
	print ("Hoje eh quinta e o dia futuro eh sabado")
elif (a == 4) and (c == 3):
	print ("Hoje eh quinta e o dia futuro eh domingo")
elif (a == 4) and (c == 4):
	print ("Hoje eh quinta e o dia futuro eh segunda")
elif (a == 4) and (c == 5):
	print ("Hoje eh quinta e o dia futuro eh terca")
elif (a == 4) and (c == 6):
	print ("Hoje eh quinta e o dia futuro eh quarta")
elif (a == 5) and (c == 0):
	print ("Hoje eh sexta e o dia futuro eh sexta")
elif (a == 5) and (c == 1):
	print ("Hoje eh sexta e o dia futuro eh sabado")
elif (a == 5) and (c == 2):
	print ("Hoje eh sexta e o dia futuro eh domingo")
elif (a == 5) and (c == 3):
	print ("Hoje eh sexta e o dia futuro eh segunda")
elif (a == 5) and (c == 4):
	print ("Hoje eh sexta e o dia futuro eh terca")
elif (a == 5) and (c == 5):
	print ("Hoje eh sexta e o dia futuro eh quarta")
elif (a == 5) and (c == 6):
	print ("Hoje eh sexta e o dia futuro eh quinta")
elif (a == 6) and (c == 0):
	print ("Hoje eh sabado e o dia futuro eh sabado")
elif (a == 6) and (c == 1):
	print ("Hoje eh sabado e o dia futuro eh domingo")
elif (a == 6) and (c == 2):
	print ("Hoje eh sabado e o dia futuro eh segunda")
elif (a == 6) and (c == 3):
	print ("Hoje eh sabado e o dia futuro eh terca")
elif (a == 6) and (c == 4):
	print ("Hoje eh sabado e o dia futuro eh quarta")
elif (a == 6) and (c == 5):
	print ("Hoje eh sabado e o dia futuro eh quinta")
else:
	print ("Hoje eh sabado e o dia futuro eh sexta")

