w = int(input("digite a data:"))

dia = w // 1000000
mes = w // 10000 % 100
ano = w % 10000

if(ano > 0):
	if(mes>0 and mes<=12):
		if((ano%400 == 0) or ((ano%100 != 0) and (ano%4 == 0))): #bissexto
			if(mes == 2 ):
				if(dia>=1 and dia<=29):
					print(dia," de ",mes," de ",ano," eh uma data valida")
				else:
					print(dia," de ",mes," de ",ano,"nao eh uma data valida")
			elif(mes == 1)or(mes == 3)or(mes == 5)or(mes == 7)or(mes == 8)or(mes == 10)or(mes == 12):
				if(dia>0 and dia<32):
					print(dia," de ",mes," de ",ano," eh uma data valida")
				else:
					print(dia," de ",mes," de ",ano," nao eh uma data valida")
			elif(mes == 4)or(mes == 6)or(mes == 9)or(mes == 11):
				if(dia>0 and dia<=30):
					print(dia," de ",mes," de ",ano," eh uma data valida")
				else:
					print(dia," de ",mes," de ",ano," nao eh uma data valida")
			else:
				print(dia," de ",mes," de ",ano," nao eh uma data valida")
		elif(mes == 2 ):
			if(dia>=1 and dia<=28):
				print(dia," de ",mes," de ",ano," eh uma data valida")
			else:
				print(dia," de ",mes," de ",ano,"nao eh uma data valida")
		elif(mes == 1)or(mes == 3)or(mes == 5)or(mes == 7)or(mes == 8)or(mes == 12):
			if(dia>0 and dia<32):
				print(dia," de ",mes," de ",ano," eh uma data valida")
			else:
				print(dia," de ",mes," de ",ano," nao eh uma data valida")
		elif(mes == 4)or(mes == 6)or(mes == 9)or(mes == 11):
			if(dia>0 and dia<=30):
				print(dia," de ",mes," de ",ano," eh uma data valida")
			else:
				print(dia," de ",mes," de ",ano," nao eh uma data valida")
		elif(mes == 10):
			if(ano == 1582):
				if(dia>0 and dia<5)or(dia>14 and dia<=31):
					print(dia," de ",mes," de ",ano," eh uma data valida")
				else:
					print(dia," de ",mes," de ",ano," nao eh uma data valida")
			else:
				if(dia>0 and dia<=31):
					print(dia," de ",mes," de ",ano," eh uma data valida")
				else:
					print(dia," de ",mes," de ",ano," nao eh uma data valida")
		else:
			print(dia," de ",mes," de ",ano," nao eh uma data valida")
	else:
		print(dia," de ",mes," de ",ano," nao eh uma data valida")
else:
	print(dia," de ",mes," de ",ano,"nao eh uma data valida")