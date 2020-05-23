from math import*

x=float(input("Digite o valor em graus:"))
y=-(1/x+2)
g=(1/(x-2))
if(x<-1000)or(x>1000):
	print("entrada invalida")
elif(x>=-1000)and(x<-2):
	print(round(y,4))
elif(x>2)and(x<=1000):
	print((round(g,4))