x=int(input("numero: "))
y=int(input("numero: "))
F=(x-y%7)
if(x==0)or(y==0):
	msg=("domingo")
elif(x==1)or(y==1):
	msg=("segunda")
elif(x==2)or(y==2):
	msg=("terça")
elif(x==3)or(y==3):
	msg=("quarta")
elif(x==4)or(y==4):
	msg=("quinta")
elif(x==5)or(y==5):
	msg=("sexta")
elif(x==6)or(y==6):
	msg=("sabado")
else:
	print("A entrada",x,"eh invalida")
print("Hoje eh",msg,"e o dia futuro eh",msg)
	
	