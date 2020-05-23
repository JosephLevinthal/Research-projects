data = int(input("Digite uma data no formato DDMMAAAA: "))
ano = data%10000
mes = (data%1000000)//10000 
dia = data//1000000

if((ano > 0) and (1 <= mes <= 12)):
	if(ano == 1582):
		if((mes == 1) and (1 <= dia <= 31)):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 2 and 1<= dia <= 28):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 3 and 1<= dia <= 31):	
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 4 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		elif(mes == 5 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		elif(mes == 6 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")		
		elif(mes == 7 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")		
		elif(mes == 8 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")			
		elif(mes == 9 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")			
		elif((mes == 10) and ((1 <= dia < 5) or (14 < dia <= 31))):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 11 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")				
		elif(mes == 12 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")				
		else:
			print(dia,"de",mes,"de",ano, "nao eh uma data valida")
	elif((ano%400 == 0) or ((ano%100 != 0) and (ano%4 == 0))):
		if((mes == 1) and (1 <= dia <= 31)):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 2 and 1<= dia <= 29):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 3 and 1<= dia <= 31):	
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 4 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		elif(mes == 5 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		elif(mes == 6 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")		
		elif(mes == 7 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")		
		elif(mes == 8 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")			
		elif(mes == 9 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")			
		elif((mes == 10 and 1 <= dia <= 31)):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 11 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")				
		elif(mes == 12 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		else:
			print(dia,"de",mes,"de",ano, "nao eh uma data valida")
	else:		
		if((mes == 1) and (1 <= dia <= 31)):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 2 and 1<= dia <= 28):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 3 and 1<= dia <= 31):	
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 4 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		elif(mes == 5 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		elif(mes == 6 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")		
		elif(mes == 7 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")		
		elif(mes == 8 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")			
		elif(mes == 9 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")			
		elif((mes == 10 and 1 <= dia <= 31)):
			print(dia,"de",mes,"de",ano, "eh uma data valida")
		elif(mes == 11 and 1<= dia <= 30):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")				
		elif(mes == 12 and 1<= dia <= 31):		
			print(dia,"de",mes,"de",ano, "eh uma data valida")	
		else:
			print(dia,"de",mes,"de",ano, "nao eh uma data valida")
else:
	print(dia,"de",mes,"de",ano, "nao eh uma data valida")