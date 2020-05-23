# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = int(input("Dia de hoje: "))
f = int(input("Numero de dias apos hoje: "))

if(p<0 or p>6):
	print("A entrada",p,"eh invalida")
elif(p+f==0 or ((f+p)%7==0)):
	ff="domingo"
	if(p==0):
		p="domingo"
	elif(p==1):
		p="segunda"
	elif(p==2):
		p="terca"
	elif(p==3):
		p="quarta"
	elif(p==4):
		p="quinta"
	elif(p==5):
		p="sexta"
	elif(p==6):
		p="sabado"
	print("Hoje eh",p,"e o dia futuro eh",ff)
elif(p+f==1 or ((f+p)%7==1)):
	ff="segunda"
	if(p==0):
		p="domingo"
	elif(p==1):
		p="segunda"
	elif(p==2):
		p="terca"
	elif(p==3):
		p="quarta"
	elif(p==4):
		p="quinta"
	elif(p==5):
		p="sexta"
	elif(p==6):
		p="sabado"
	print("Hoje eh",p,"e o dia futuro eh",ff)
elif(p+f==2 or ((f+p)%7==2)):
	ff="terca"
	if(p==0):
		p="domingo"
	elif(p==1):
		p="segunda"
	elif(p==2):
		p="terca"
	elif(p==3):
		p="quarta"
	elif(p==4):
		p="quinta"
	elif(p==5):
		p="sexta"
	elif(p==6):
		p="sabado"
	print("Hoje eh",p,"e o dia futuro eh",ff)
elif(p+f==3 or ((f+p)%7==3)):
	ff="quarta"
	if(p==0):
		p="domingo"
	elif(p==1):
		p="segunda"
	elif(p==2):
		p="terca"
	elif(p==3):
		p="quarta"
	elif(p==4):
		p="quinta"
	elif(p==5):
		p="sexta"
	elif(p==6):
		p="sabado"
	print("Hoje eh",p,"e o dia futuro eh",ff)
elif(p+f==4 or ((f+p)%7==4)):
	ff="quinta"
	if(p==0):
		p="domingo"
	elif(p==1):
		p="segunda"
	elif(p==2):
		p="terca"
	elif(p==3):
		p="quarta"
	elif(p==4):
		p="quinta"
	elif(p==5):
		p="sexta"
	elif(p==6):
		p="sabado"
	print("Hoje eh",p,"e o dia futuro eh",ff)
elif(p+f==5 or ((f+p)%7==5)):
	ff="sexta"
	if(p==0):
		p="domingo"
	elif(p==1):
		p="segunda"
	elif(p==2):
		p="terca"
	elif(p==3):
		p="quarta"
	elif(p==4):
		p="quinta"
	elif(p==5):
		p="sexta"
	elif(p==6):
		p="sabado"
	print("Hoje eh",p,"e o dia futuro eh",ff)
elif(p+f==6 or ((f+p)%7==6)):
	ff="sabado"
	if(p==0):
		p="domingo"
	elif(p==1):
		p="segunda"
	elif(p==2):
		p="terca"
	elif(p==3):
		p="quarta"
	elif(p==4):
		p="quinta"
	elif(p==5):
		p="sexta"
	elif(p==6):
		p="sabado"
	print("Hoje eh",p,"e o dia futuro eh",ff)