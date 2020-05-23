from math import*
x=float(input("valor: "))
if(x>=-4)and(x<0):
	msg=(abs(x)**(1/2))
elif(x==0):
	msg=(0)
elif(x>0)and(x<=4):
	msg=(x**(1/2))
else:
	msg=("entrada invalida")
print(round(msg, 4))