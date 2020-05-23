# Ao testar sua solução, não se limite ao caso de exemplo.
m = int(input("digite um numero: "))

if ((m > 12) or (m < 0)):
	print("numero de mes invalido")
elif (m == 1):
	print("janeiro")
elif (m == 2):
	print("fevereiro")
elif (m == 3):
	print("marco")
elif (m == 4):
	print("abril")
elif (m == 5):
	print("maio")
elif (m == 6):
	print("junho")
elif (m == 7):
	print("julho")
elif (m == 8):
	print("agosto")
elif (m == 9):
	print("setembro")
elif (m == 10):
	print("outubro")
elif (m == 11):
	print("novembro")
else:
	print("dezembro")