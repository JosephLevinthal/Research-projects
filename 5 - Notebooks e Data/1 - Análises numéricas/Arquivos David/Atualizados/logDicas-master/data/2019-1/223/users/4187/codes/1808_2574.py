senha = input("digite um sennha:")
M =0
m = 0

for i in range(0,len(senha)):
	if(senha[i].isupper()):
		M = M + 1
	elif(senha[i].islower()):
		m = m + 1
if(len(senha) >= 8 and m >= 1 and M >= 1):
	print("SENHA VALIDA")
else:
	print("SENHA INVALIDA")