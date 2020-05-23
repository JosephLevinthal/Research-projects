from numpy import*
a=input("string: ")
for i in range(len(a)):
	if(a[i].isupper()==1 and a[i].islower()==1):
		print("SENHA VALIDA")
print("SENHA INVALIDA")