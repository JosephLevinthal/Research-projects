# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

h= int(input(": "))
f = int(input("dia futuro: "))

a = (h+f)%7


if(h == 0):
	h = "domingo"
elif(h == 1):
	h = "segunda"
elif( h == 2):
	h= "terca"
elif(h == 3):
	h= "quarta"
elif(h == 4):
	h= "quinta"
elif(h == 5):
	h= "sexta"
elif(h == 6):
	h= "sabado"
else:
	print("A entrada",h,"eh invalida")

if (h==0)or(h==2)or(h==3)or(h!=4)or(h==5)or(h==6):
	elif(a == 0):
	y= "domingo"
	print("Hoje eh",h,"e o dia futuro eh",y)
elif(a == 1):
	y= "segunda"
	print("Hoje eh",h,"e o dia futuro eh",y)
elif(a == 2):
	y= "terca"
	print("Hoje eh",h,"e o dia futuro eh",y)
elif(a == 3):
	y="quarta"
	print("Hoje eh",h,"e o dia futuro eh",y)
elif(a == 4):
	y= "quinta"
	print("Hoje eh",h,"e o dia futuro eh",y)
elif(a == 5):
	y= "sexta"
	print("Hoje eh",h,"e o dia futuro eh",y)
elif(a==6):
	y = ("sabado")	
	print("Hoje eh",h,"e o dia futuro eh",y)
else:
	print("A entrada",h,"eh invalida")