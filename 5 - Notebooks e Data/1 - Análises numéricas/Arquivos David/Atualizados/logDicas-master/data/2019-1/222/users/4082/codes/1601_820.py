# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016





VALOR = input()
if VALOR>0 and VALOR%2==0:
	nota50 = VALOR//50
	aux1 = nota50*50
	nota10 = (VALOR - aux1)//10
	aux2 = nota10*10
	nota2 = (valor- aux1- aux2)//2
	print(nota50)
	print(nota10)
	print(nota2)
	
