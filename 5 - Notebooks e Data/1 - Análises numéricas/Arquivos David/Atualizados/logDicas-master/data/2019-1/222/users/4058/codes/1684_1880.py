# Ao testar sua solução, não se limite ao caso de exemplo.
num = int(input("valor: "))
if num>=1 and num <= 12:
	if num == 1:
		print("janeiro")
	elif num == 2:
		print("fevereiro")
	elif num == 3:
		print("marco")
	elif num == 4:
		print("abril")
	elif num == 5:
		print("maio")
	elif num == 6:
		print("junho")
	elif num ==7:
		print("julho")
	elif num ==8:
		print("agosto")
	elif num ==9:
		print("setembro")
	elif num==10:
		print("outubro")
	elif num==11:
		print("novembro")
	else:
		print("dezembro")
else:
	print("numero de mes invalido")