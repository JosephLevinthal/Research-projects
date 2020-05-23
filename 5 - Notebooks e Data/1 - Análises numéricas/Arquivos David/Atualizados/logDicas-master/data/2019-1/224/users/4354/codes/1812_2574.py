from numpy import *
senha = input("digite a senha: ")
if(len(senha) >= 8):
	maiu = 0
	minu = 0
	for j,i in zip(senha,senha):
		if(i.islower() == True):
			minu = minu + 1
		if(i.isupper() == True):
			maiu = maiu + 1
	if(maiu > 0 and minu > 0):
		print("SENHA VALIDA")
	else:
		print("SENHA INVALIDA")
else:
	print("SENHA INVALIDA")