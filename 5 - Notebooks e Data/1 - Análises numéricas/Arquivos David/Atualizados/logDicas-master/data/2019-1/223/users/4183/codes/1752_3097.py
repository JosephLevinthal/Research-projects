pos = 1
pon = 0
while (not pos == 0):
	pos = int(input("Digite: "))
	if (pos == 1):
		pon = 25
		cont = cont + 1
	elif (pos == 2):
		pon = 18
		cont = cont + 1
	elif (pos == 3):
		pon = 12
		cont = cont + 1
	elif (pos == 6):
		pon == 8
		cont = cont + 1
	elif (pos > 4 and pos < 10):
		pon = 14
pon = pon * 10
print(pon)
		