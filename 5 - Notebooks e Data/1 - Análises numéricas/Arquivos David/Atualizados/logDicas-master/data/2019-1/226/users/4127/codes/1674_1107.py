# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x= int(input("qual seu numero da semana?"))
y= int(input("qual seu dia do futuro? "))
s=x+y
if(s>=6):
	h=s%7
else:
	h= s
if (h==0):
	dia="domingo"
elif (h==1):
	dia="segunda"
elif(h==2):
	dia="terca"
elif(h==3):
	dia="quarta"
elif(h==4):
	dia="quinta"
elif(h==5):
	dia="sexta"
elif(h==6):
	dia="sabado"

if not(0<=x<=6):
	print("A entrada", x, "eh invalida")
if (x==0):
	diaf="domingo"
	print("Hoje eh",diaf,"e o dia futuro eh",dia)
elif (x==1):
	diaf="segunda"
	print("Hoje eh",diaf,"e o dia futuro eh",dia)
elif(x==2):
	diaf="terca"
	print("Hoje eh",diaf,"e o dia futuro eh",dia)
elif(x==3):
	diaf="quarta"
	print("Hoje eh",diaf,"e o dia futuro eh",dia)
elif(x==4):
	diaf="quinta"
	print("Hoje eh",diaf,"e o dia futuro eh",dia)
elif(x==5):
	diaf="sexta"
	print("Hoje eh",diaf,"e o dia futuro eh",dia)
elif(x==6):
	diaf="sabado"
	print("Hoje eh",diaf,"e o dia futuro eh",dia)


