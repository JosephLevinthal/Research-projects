# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir sd
dia = int(input())
diaf = int(input())
diae = (diaf-dia)%6
if(dia>6 or dia<0):
	print("A entrada", dia, "eh invalida")
else:
	if(dia==0):
		hoje = "domingo"
	elif(dia==1):
		hoje = "segunda"
	elif(dia==2):
		hoje = "terca"
	elif(dia==3):
		hoje = "quarta"
	elif(dia==4):
		hoje = "quinta"
	elif(dia==5):
		hoje = "sexta"
	else:
		hoje = "sabado"

if(diae==0):
	futuro = "domingo"
elif(diae==1):
	futuro = "segunda"
elif(diae==2):
	futuro = "terca"
elif(diae==3):
	futuro = "quarta"
elif(diae==4):
	futuro = "quinta"
elif(diae==5):
	futuro = "sexta"
elif(diae==6):
	futuro = "sabado"
print("Hoje eh", hoje," e o dia futuro eh", futuro)


	