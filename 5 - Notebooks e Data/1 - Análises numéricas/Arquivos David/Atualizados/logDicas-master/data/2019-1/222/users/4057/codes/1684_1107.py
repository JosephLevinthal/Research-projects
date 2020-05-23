# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = int(input("Entre com o numero do dia de hoje: 0 a 6"))
y = int(input("Entre com o numero de dias apos hoje: "))

if x >= 0 and x<= 6:
	if x == 0:
		if y == 0:
			x = "domingo"
			y = "domingo"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 1:
			x = "domingo"
			y = "segunda"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 2:
			x = "domingo"
			y = "terca"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 3 :
			x = "domingo"
			y = "quarta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 4: 
			x = "domingo"
			y = "quinta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 5 :
			x = "domingo"
			y = "sexta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 6 : 
			x = "domingo"
			y = "sabado"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y >= 7 :
			a = y % 7
			if a == 0:
				x = "domingo"
				a = "domingo"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 1 :
				x = "domingo"
				a = "segunda"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 2 :
				x = "domingo"
				a = "terca"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif y == 3 :
				x = "domingo"
				a = "quarta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 4: 
				x = "domingo"
				a = "quinta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 5 :
				x = "domingo"
				a = "sexta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 6 : 
				x = "domingo"
				a = "sabado"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			else :
				print("A entrada eh invalida")
		else:
			print("A entrada eh invalida")
		
	elif x == 1:
		if y == 0 :
			x = "segunda"
			y = "segunda"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 1 :
			x = "segunda"
			y = "terca"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 2 :
			x = "segunda"
			y = "quarta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 3 :
			x = "segunda"
			y = "quinta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 4: 
			x = "segunda"
			y = "sexta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 5 :
			x = "segunda"
			y = "sabado"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 6 : 
			x = "segunda"
			y = "domingo"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y >= 7 :
			a = y % 7
			if a == 0:
				x = "segunda"
				a = "segunda"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 1 :
				x = "segunda"
				a = "terca"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 2 :
				x = "segunda"
				a = "quarta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 3 :
				x = "segunda"
				a = "quinta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 4: 
				x = "segunda"
				a = "sexta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 5 :
				x = "segunda"
				a = "sabado"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 6 : 
				x = "segunda"
				a = "domingo"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			else:
				print("A entrada eh invalida")
		else: 
			print("A entrada eh invalida")
		
	elif x == 2:
		if y == 0:
			x = "terca"
			y = "terca"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 1 :
			x = "terca"
			y = "quarta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 2 :
			x = "terca"
			y = "quinta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 3 :
			x = "terca"
			y = "sexta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 4: 
			x = "terca"
			y = "sabado"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 5 :
			x = "terca"
			y = "domingo"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 6 : 
			x = "terca"
			y = "segunda"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y >= 7 :
			a = y % 7
			if a == 0 :
				x = "terca"
				a = "terca"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 1 :
				x = "terca"
				a = "quarta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 2 :
				x = "terca"
				a = "quinta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 3 :
				x = "terca"
				a = "sexta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 4: 
				x = "terca"
				a = "sabado"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 5 :
				x = "terca"
				a = "domingo"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 6 : 
				x = "terca"
				a = "segunda"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			else: 
				print("A entrada eh invalida")
		else:
			print("A entrada eh invalida")
	elif x == 3:
		if y == 0:
			x = "quarta"
			y = "quarta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 1 :
			x = "quarta"
			y = "quinta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 2 :
			x = "quarta"
			y = "sexta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 3 :
			x = "quarta"
			y = "sabado"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 4: 
			x = "quarta"
			y = "domingo"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 5 :
			x = "quarta"
			y = "segunda"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 6 : 
			x = "quarta"
			y = "terca"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y >= 7 :
			a = y % 7
			if a== 0:
				x = "quarta"
				a = "quarta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 1 :
				x = "quarta"
				a = "quinta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 2 :
				x = "quarta"
				a = "sexta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 3 :
				x = "quarta"
				a = "sabado"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 4: 
				x = "quarta"
				a = "domingo"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 5 :
				x = "quarta"
				a = "segunda"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 6 : 
				x = "quarta"
				a = "terca"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			else:
				print("A entrada eh invalida")
		else: 
			print("A entrada eh invalida")
	elif x == 4:
		if y == 0 :
			x = "quinta"
			y = "quinta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 1 :
			x = "quinta"
			y = "sexta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 2 :
			x = "quinta"
			y = "sabado"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 3 :
			x = "quinta"
			y = "domingo"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 4: 
			x = "quinta"
			y = "segunda"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 5 :
			x = "quinta"
			y = "terca"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 6 : 
			x = "quinta"
			y = "quarta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y >= 7 :
			a = y % 7
			if a == 0:
				x = "quinta"
				a = "quinta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 1 :
				x = "quinta"
				a = "sexta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 2 :
				x = "quinta"
				a = "sabado"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 3 :
				x = "quinta"
				a = "domingo"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 4: 
				x = "quinta"
				a = "segunda"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 5: 
				x = "quinta"
				a = "terca"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 6 : 
				x = "quinta"
				a = "quarta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			else: 
				print("A entrada eh invalida")
		else:
			print("A entrada eh invalida")
	elif x == 5:
		if y == 0: 
			x = "sexta"
			y = "sexta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 1 :
			x = "sexta"
			y = "sabado"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 2 :
			x = "sexta"
			y = "domingo"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 3 :
			x = "sexta"
			y = "segunda"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 4: 
			x = "sexta"
			y = "terca"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 5 :
			x = "sexta"
			y = "quarta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 6 : 
			x = "sexta"
			y = "quinta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y >= 7 :
			a = y % 7
			if a == 0:
				x = "sexta"
				a = "sexta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 1 :
				x = "sexta"
				a = "sabado"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 2 :
				x = "sexta"
				a = "domingo"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 3 :
				x = "sexta"
				a = "segunda"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 4: 
				x = "sexta"
				a = "terca"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 5 :
				x = "sexta"
				a = "quarta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 6 : 
				x = "sexta"
				a = "quinta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			else: 
				print("A entrada eh invalida")
		else:
			print("A entrada eh invalida")
		
	elif x == 6:
		if y == 0:
			x = "sabado"
			y = "sabado"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 1 :
			x = "sabado"
			y = "domingo"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 2 :
			x = "sabado"
			y = "segunda"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 3 :
			x = "sabado"
			y = "terca"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 4: 
			x = "sabado"
			y = "quarta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 5 :
			x = "sabado"
			y = "quinta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y == 6 : 
			x = "sabado"
			y = "sexta"
			print("Hoje eh ", x, "e o dia futuro eh ", y)
		elif y >= 7 :
			a = y % 7
			if a == 0 :
				x = "sabado"
				a = "sabado"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 1 :
				x = "sabado"
				a = "domingo"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 2 :
				x = "sabado"
				a = "segunda"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 3 :
				x = "sabado"
				a = "terca"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 4: 
				x = "sabado"
				a = "quarta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 5 :
				x = "sabado"
				a = "quinta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			elif a == 6 : 
				x = "sabado"
				a = "sexta"
				print("Hoje eh ", x, "e o dia futuro eh ", a)
			else: 
				print("A entrada eh invalida")
		else: 
			print("A entrada eh invalida")
else :
	print("A entrada ", x, "eh invalida")