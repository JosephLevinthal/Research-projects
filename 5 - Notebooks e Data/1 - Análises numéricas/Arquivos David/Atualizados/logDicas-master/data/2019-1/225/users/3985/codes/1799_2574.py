from numpy import*

a=input()
b=0
c=0
for i in range(len(a)):
	if (a[i].islower()):
		b += 1
	elif (a[i].isupper()):
		c+=1
if(len(a)>=8 and b >0 and c>0):
	print("SENHA VALIDA")
else:
	print("SENHA INVALIDA")