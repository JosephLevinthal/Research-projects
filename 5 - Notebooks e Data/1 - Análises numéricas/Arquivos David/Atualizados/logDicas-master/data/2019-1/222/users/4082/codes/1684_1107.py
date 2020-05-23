# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

dia = int(input("Numero do dia de hoje:"))
dp = int(input("Numero do dias apos hoje:"))




resto = dp % 7


df =(resto + dia)%7


if (dias==0):
	hoje = 'domingo'
elif (dia ==1):
	hoje = 'segunda'
elif(dia ==2):
	hoje = ' terca'
elif (dia ==3):
		hoje = 'quarta'
elif(dia ==4):
	hoje = 'quinta'
elif (dia ==5):
	hoje = 'sexta'
elif (dia ==6):
	hoje= 'sabado'
else:
	hoje= 'invalido'
if(df ==0):
	diaf='domingo'
elif(df ==1):
		diaf='segunda'
elif(df ==2):
	diaf='terca'
elif(df ==3):
	diaf='quarta'
elif(df ==4):
	diaf='quinta'
elif(df ==5):
	diaf='sexta'
elif(df ==6):
	diaf='sabado'
	
print("Hoje eh {} e o dia fituro eh {}".format(hoje,diaf))

else:
	
print("A entrada {} eh invalida".format(dia))