from numpy import *
senha=input()
a=0
b=0
for i in range(len(senha)):
	if(senha[i].islower()):
		a=a+1
	if(senha[i].isupper()):
		b=b+1
if(len(senha)>=8 and a!=0 and b!=0 ):
	print("SENHA VALIDA")
else: 
	print("SENHA INVALIDA")
