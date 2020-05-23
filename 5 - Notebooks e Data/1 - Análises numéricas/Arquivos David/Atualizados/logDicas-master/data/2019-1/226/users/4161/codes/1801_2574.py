senha = input("senha: ")
n = len(senha)
a = 0
b = 0
for x in senha:
	if not(x.isnumeric()):
		if x.islower():
			a = a + 1
		elif x.isupper():
			b = b + 1
if (n<8):
	print("SENHA INVALIDA")
elif not(a>0) or not(b>0):
	print("SENHA INVALIDA")
else:
	print("SENHA VALIDA")
