from numpy import *

senha = input("Informe a senha: ")

tamanho = 8

while tamanho >= len(senha):
	
	for i in range(len(senha)):
		
		if senha[i].islower() and senha[i].isupper() and len(senha) >=8:
			valida = "SENHA VALIDA"
		else:
			valida = "SENHA INVALIDA"
	
	print(valida)
			
	