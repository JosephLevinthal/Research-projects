X0=float(input("Digite Xo: "))
Y0=float(input("Digite Yo: "))
X1=float(input("Digite X1: "))
Y1=float(input("Digite Y2: "))
X2=float(input("Digite X2: "))
Y2=float(input("Digite Y2: "))
c =(X1 - X0)*(Y2-Y0)-(X2-X0)*(Y1-Y0)
if(c<0):
	mensagem ="A direita da reta"
	print(mensagem)
elif(c>0):
	mensagem="A esquerda da reta"
	print(mensagem)
elif(c==0):
	mensagem="Sobre a reta"
	print(mensagem)

