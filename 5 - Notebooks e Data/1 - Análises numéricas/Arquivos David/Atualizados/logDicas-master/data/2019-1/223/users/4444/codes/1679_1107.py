hoje= int(input('que dia e hoje:  '))
futuro=int(input('que dia do futuro: '))
resto= futuro % 7

#hoje igual a zero relaciona-se ao dia da semana - neste caso, domingo.
#resto relaciona-se ao dia do futuro n % 7
if((hoje < 0) or (hoje > 6)):
	print("A entrada", hoje, "eh invalida")
elif(hoje==0):
	if(resto == 0):
		print('Hoje eh domingo e o dia futuro eh domingo')
	elif(resto == 1):
		print('Hoje eh domingo e o dia futuro eh segunda')
	elif(resto == 2):
		print('Hoje eh domingo e o dia futuro eh terca')
	elif(resto == 3):
		print('Hoje eh domingo e o dia futuro eh quarta')
	elif(resto == 4):
		print('Hoje eh domingo e o dia futuro eh quinta')
	elif(resto == 5):
		print('Hoje eh domingo e o dia futuro eh sexta')
	elif(resto == 6):
		print('Hoje eh domingo e o dia futuro eh sabado')
elif(hoje == 1):
	if(resto == 0):
		print('Hoje eh segunda e o dia futuro eh segunda')
	elif(resto == 1):
		print('Hoje eh segunda e o dia futuro eh terca')
	elif(resto == 2):
		print('Hoje eh segunda e o dia futuro eh quarta ')
	elif(resto == 3):
		print('Hoje eh segunda e o dia futuro eh quinta')
	elif(resto == 4):
		print('Hoje eh segunda e o dia futuro eh sexta')
	elif(resto == 5):
		print('Hoje eh segunda e o dia futuro eh sabado')
	elif(resto == 6):
		print('Hoje eh segunda e o dia futuro eh domingo')
elif(hoje==2):
	if(resto == 0):
		print('Hoje eh terca e o dia futuro eh terca')
	elif(resto == 1):
		print('Hoje eh terca e o dia futuro eh quarta')
	elif(resto == 2):
		print('Hoje eh terca e o dia futuro eh quinta ')
	elif(resto == 3):
		print('Hoje eh terca e o dia futuro eh sexta')
	elif(resto == 4):
		print('Hoje eh terca e o dia futuro eh sabado')
	elif(resto == 5):
		print('Hoje eh terca e o dia futuro eh domingo')
	elif(resto == 6):
		print('Hoje eh terca e o dia futuro eh segunda')
	
elif(hoje==3):
	if(resto == 0):
		print('Hoje eh quarta e o dia futuro eh quarta')
	elif(resto == 1):
		print('Hoje eh quarta e o dia futuro eh quinta')
	elif(resto == 2):
		print('Hoje eh quarta e o dia futuro eh sexta ')
	elif(resto == 3):
		print('Hoje eh quarta e o dia futuro eh sabado')
	elif(resto == 4):
		print('Hoje eh quarta e o dia futuro eh domingo')
	elif(resto == 5):
		print('Hoje eh quarta e o dia futuro eh segunda')
	elif(resto == 6):
		print('Hoje eh quarta e o dia futuro eh terca')
	
#######
elif(hoje == 4):
	if(resto == 0):
		print('Hoje eh quinta e o dia futuro eh quinta')
	elif(resto == 1):
		print('Hoje eh quinta e o dia futuro eh sexta')
	elif(resto == 2):
		print('Hoje eh quinta e o dia futuro eh sabado ')
	elif(resto == 3):
		print('Hoje eh quinta e o dia futuro eh domingo')
	elif(resto == 4):
		print('Hoje eh quinta e o dia futuro eh segunda')
	elif(resto == 5):
		print('Hoje eh quinta e o dia futuro eh terca')
	elif(resto == 6):
		print('Hoje eh quinta e o dia futuro eh quarta')
	
#######
elif(hoje==5):
	if(resto == 0):
		print('Hoje eh sexta e o dia futuro eh sexta')
	elif(resto == 1):
		print('Hoje eh sexta e o dia futuro eh sabado')
	elif(resto == 2):
		print('Hoje eh sexta e o dia futuro eh domingo')
	elif(resto == 3):
		print('Hoje eh sexta e o dia futuro eh segunda')
	elif(resto == 4):
		print('Hoje eh sexta e o dia futuro eh terca')
	elif(resto == 5):
		print('Hoje eh sexta e o dia futuro eh quarta')
	elif(resto == 6):
		print('Hoje eh sexta e o dia futuro eh quinta')
	

elif(hoje==6):
	if(resto == 0):
		print('Hoje eh sabado e o dia futuro eh sabado')
	elif(resto == 1):
		print('Hoje eh sabado e o dia futuro eh domingo')
	elif(resto == 2):
		print('Hoje eh sabado e o dia futuro eh segunda ')
	elif(resto == 3):
		print('Hoje eh sabado e o dia futuro eh terca')
	elif(resto == 4):
		print('Hoje eh sabado e o dia futuro eh quarta')
	elif(resto == 5):
		print('Hoje eh sabado e o dia futuro eh quinta')
	elif(resto == 6):
		print('Hoje eh sabado e o dia futuro eh sexta')
		
