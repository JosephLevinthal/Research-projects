# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
d=int(input("Digite o dia: "))
if(d>=0 and d<=6):
	a = int(input("Digite os dias futuros: "))
	f=(d+a)%7
	if(d==0):
		d="domingo"
	elif(d==1):
		d="segunda"
	elif(d==2):
		d="terca"
	elif(d==3):
		d="quarta"
	elif(d==4):
		d="quinta"
	elif(d==5):
		d="sexta"
	else:
		d="sabado"
	
	if(f==0):
		f="domingo"
	elif(f==1):
		f="segunda"
	elif(f==2):
		f="terca"
	elif(f==3):
		f="quarta"
	elif(f==4):
		f="quinta"
	elif(f==5):
		f="sexta"
	else:
		f="sabado"
	print("Hoje eh", d, "e o dia futuro eh", f)
else:
	print("A entrada",d, "eh invalida")
		