N = input()
minu = False
maiu = False
	for i in range(len(N)):
		if N[i].islower():
			minu = True
		elif N[i].isupper():
			maiu = True
if (minu == True and maiu == True and len(N) >= 8):
	print("SENHA VALIDA")
else:
	print("SENHA INVALIDA")
		