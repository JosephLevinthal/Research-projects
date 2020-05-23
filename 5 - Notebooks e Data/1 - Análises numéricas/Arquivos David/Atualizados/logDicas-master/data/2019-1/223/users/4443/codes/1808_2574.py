from numpy import *
senha = input("Digite uma senha: ")
n = len(senha)
mai = 0
minu = 0
for i in range(n):
	if(senha[i].islower() == True):
		minu = minu+1 
	else: 
		mai = mai+1
if(n >= 8 and mai >= 1 and minu >= 1):
	print("SENHA VALIDA")
else:
	print("SENHA INVALIDA")