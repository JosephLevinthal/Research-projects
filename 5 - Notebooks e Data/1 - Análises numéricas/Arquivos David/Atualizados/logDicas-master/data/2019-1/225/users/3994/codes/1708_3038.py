from math import*
x=float(input("Digite x: "))
if(x<-1 or x==-1 or x>1 or x==1):
	mensagem=abs((x)**0.5)
	print(round((mensagem),2))
elif(x==0):
	mensagem=0
	print(mensagem)
elif(x>-1 and x<0 or x>0 and x<1):
	mensagem=abs(x)
	print(round((mensagem),2))
