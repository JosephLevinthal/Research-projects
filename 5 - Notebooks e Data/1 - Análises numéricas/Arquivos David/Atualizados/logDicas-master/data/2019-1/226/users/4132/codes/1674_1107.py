# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("Digite x: "))
y = int(input("Digite y: "))

dia2 = (x+y)%7

if( x >= 0 and x <= 6):
	if(x==0):
			dia = "domingo"
			if(dia2==0):
				dia2="domingo"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==1):
				dia2="segunda"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==2):
				dia2="terca"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==3):
				dia2="quarta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==4):
				dia2=="quinta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==5):
				dia2="sexta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==6):
				dia2="sabado"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
	elif(x==1):
			dia = "segunda"
			if(dia2==0):
				dia2="domingo"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==1):
				dia2="segunda"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==2):
				dia2="terca"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==3):
				dia2="quarta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==4):
				dia2=="quinta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==5):
				dia2="sexta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==6):
				dia2="sabado"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
	elif(x==2):
			dia = "terca"
			if(dia2==0):
				dia2="domingo"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==1):
				dia2="segunda"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==2):
				dia2="terca"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==3):
				dia2="quarta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==4):
				dia2=="quinta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==5):
				dia2="sexta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==6):
				dia2="sabado"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
	elif(x==3):
			dia = "quarta"
			if(dia2==0):
				dia2="domingo"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==1):
				dia2="segunda"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==2):
				dia2="terca"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==3):
				dia2="quarta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==4):
				dia2=="quinta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==5):
				dia2="sexta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==6):
				dia2="sabado"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
	elif(x==4):
			dia = "quinta"
			if(dia2==0):
				dia2="domingo"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==1):
				dia2="segunda"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==2):
				dia2="terca"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==3):
				dia2="quarta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==4):
				dia2=="quinta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==5):
				dia2="sexta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==6):
				dia2="sabado"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
	elif(x==5):
			dia = "sexta"
			if(dia2==0):
				dia2="domingo"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==1):
				dia2="segunda"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==2):
				dia2="terca"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==3):
				dia2="quarta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==4):
				dia2=="quinta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==5):
				dia2="sexta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==6):
				dia2="sabado"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
	elif(x==6):
			dia = "sabado"
			if(dia2==0):
				dia2="domingo"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==1):
				dia2="segunda"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==2):
				dia2="terca"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==3):
				dia2="quarta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==4):
				dia2=="quinta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==5):
				dia2="sexta"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
			elif(dia2==6):
				dia2="sabado"
				print("Hoje eh",dia,"e o dia futuro eh",dia2)
else:
	print("A entrada",x,
			"eh invalida")