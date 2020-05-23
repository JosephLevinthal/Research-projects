from numpy import*
s=input("Insira sua senha :")

for i in range(len(s)):
	if(s[i].islower()):
		if(s[i].isupper()):
			if(len(s)>=8):
print("SENHA VALIDA")
	else:
print("SENHA INVALIDA")
		