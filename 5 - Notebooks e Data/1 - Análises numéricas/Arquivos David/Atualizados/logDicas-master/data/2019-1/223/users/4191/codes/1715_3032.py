import math
x=float(input("Valor de x: "))
if(x<=0):
	funcao=0
	print(funcao)
elif((x>0)and(x<=1)):
	funcao=1
	print(funcao)
elif((x>1)and(x<=2)):
	funcao=x**(1/2)
	print(round(funcao ,4))
elif(x>2):
	funcao=x**(1/3)
	print(round(funcao, 4))