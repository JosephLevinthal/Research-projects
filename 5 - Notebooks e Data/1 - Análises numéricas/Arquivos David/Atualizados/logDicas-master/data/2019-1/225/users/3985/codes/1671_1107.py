# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x= int(input("HJ: "))
v= int(input("Dia do fut: "))
 
if ((x+v)%7 == 0):
	s= "domingo"
elif ((x+v)%7 == 1):
	s= "segunda"
elif ((x+v)%7 == 2):
	s= "terca"
elif ((x+v)%7 == 3):
	s= "quarta"
elif ((x+v)%7 == 4):
	s= "quinta"
elif ((x+v)%7 == 5):
	s= "sexta"
elif ((x+v)%7 == 6):
	s= "sabado"
if (x<0) or (x>6):
	print("A entrada",x,"eh invalida")
elif (x==0):
	print("Hoje eh domingo e o dia futuro eh", s)
elif (x==1):
	print("Hoje eh segunda e o dia futuro eh", s)
elif (x==2):
	print("Hoje eh terca e o dia futuro eh", s)
elif (x==3):
	print("Hoje eh quarta e o dia futuro eh", s)
elif (x==4):
	print("Hoje eh quinta e o dia futuro eh", s)
elif (x==5):
	print("Hoje eh sexta e o dia futuro eh", s)
elif (x==6):
	print("Hoje eh sabado e o dia futuro eh", s)