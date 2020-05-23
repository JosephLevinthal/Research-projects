# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=int(input("numero     "))
y=int(input("futuro     "))
z=x+y
if(x<0)or(x>6):
	print("A entrada ",x," eh invalida")
else:
	if(x==0):
		if((z)%(7))==0:
			print("Hoje eh domingo e o dia futuro eh domingo")
		elif((z)%(7))==1:
			print("Hoje eh domingo e o dia futuro eh segunda")
		elif((z)%(7))==2:
			print("Hoje eh domingo e o dia futuro eh terca")
		elif((z)%(7))==3:
			print("Hoje eh domingo e o dia futuro eh quarta")
		elif((z)%(7))==4:
			print("Hoje eh domingo e o dia futuro eh quinta")
		elif((z)%(7))==5:
			print("Hoje eh domingo e o dia futuro eh sexta")
		elif((z)%(7))==6:
			print("Hoje eh domingo e o dia futuro eh sabado")
	elif(x==1):
		if((z)%(7))==0:
			print("Hoje eh segunda e o dia futuro eh domingo")
		elif((z)%(7))==1:
			print("Hoje eh segunda e o dia futuro eh segunda")
		elif((z)%(7))==2:
			print("Hoje eh segunda e o dia futuro eh terca")
		elif((z)%(7))==3:
			print("Hoje eh segunda e o dia futuro eh quarta")
		elif((z)%(7))==4:
			print("Hoje eh segunda e o dia futuro eh quinta")
		elif((z)%(7))==5:
			print("Hoje eh segunda e o dia futuro eh sexta")
		elif((z)%(7))==6:
			print("Hoje eh segunda e o dia futuro eh sabado")
	elif(x==2):
		if((z)%(7))==0:
			print("Hoje eh terca e o dia futuro eh domingo")
		elif((z)%(7))==1:
			print("Hoje eh terca e o dia futuro eh segunda")
		elif((z)%(7))==2:
			print("Hoje eh terca e o dia futuro eh terca")
		elif((z)%(7))==3:
			print("Hoje eh terca e o dia futuro eh quarta")
		elif((z)%(7))==4:
			print("Hoje eh terca e o dia futuro eh quinta")
		elif((z)%(7))==5:
			print("Hoje eh terca e o dia futuro eh sexta")
		elif((z)%(7))==6:
			print("Hoje eh terca e o dia futuro eh sabado")
	elif(x==3):
		if((z)%(7))==0:
			print("Hoje eh quarta e o dia futuro eh domingo")
		elif((z)%(7))==1:
			print("Hoje eh quarta e o dia futuro eh segunda")
		elif((z)%(7))==2:
			print("Hoje eh quarta e o dia futuro eh terca")
		elif((z)%(7))==3:
			print("Hoje eh quarta e o dia futuro eh quarta")
		elif((z)%(7))==4:
			print("Hoje eh quarta e o dia futuro eh quinta")
		elif((z)%(7))==5:
			print("Hoje eh quarta e o dia futuro eh sexta")
		elif((z)%(7))==6:
			print("Hoje eh quarta e o dia futuro eh sabado")
	elif(x==4):
		if((z)%(7))==0:
			print("Hoje eh quinta e o dia futuro eh domingo")
		elif((z)%(7))==1:
			print("Hoje eh quinta e o dia futuro eh segunda")
		elif((z)%(7))==2:
			print("Hoje eh quinta e o dia futuro eh terca")
		elif((z)%(7))==3:
			print("Hoje eh quinta e o dia futuro eh quarta")
		elif((z)%(7))==4:
			print("Hoje eh quinta e o dia futuro eh quinta")
		elif((z)%(7))==5:
			print("Hoje eh quinta e o dia futuro eh sexta")
		elif((z)%(7))==6:
			print("Hoje eh quinta e o dia futuro eh sabado")
	elif(x==5):
		if((z)%(7))==0:
			print("Hoje eh sexta e o dia futuro eh domingo")
		elif((z)%(7))==1:
			print("Hoje eh sexta e o dia futuro eh segunda")
		elif((z)%(7))==2:
			print("Hoje eh sexta e o dia futuro eh terca")
		elif((z)%(7))==3:
			print("Hoje eh sexta e o dia futuro eh quarta")
		elif((z)%(7))==4:
			print("Hoje eh sexta e o dia futuro eh quinta")
		elif((z)%(7))==5:
			print("Hoje eh sexta e o dia futuro eh sexta")
		elif((z)%(7))==6:
			print("Hoje eh sexta e o dia futuro eh sabado")
	elif(x==6):
		if((z)%(7))==0:
			print("Hoje eh sabado e o dia futuro eh domingo")
		elif((z)%(7))==1:
			print("Hoje eh sabado e o dia futuro eh segunda")
		elif((z)%(7))==2:
			print("Hoje eh sabado e o dia futuro eh terca")
		elif((z)%(7))==3:
			print("Hoje eh sabado e o dia futuro eh quarta")
		elif((z)%(7))==4:
			print("Hoje eh sabado e o dia futuro eh quinta")
		elif((z)%(7))==5:
			print("Hoje eh sabado e o dia futuro eh sexta")
		elif((z)%(7))==6:
			print("Hoje eh sabado e o dia futuro eh sabado")