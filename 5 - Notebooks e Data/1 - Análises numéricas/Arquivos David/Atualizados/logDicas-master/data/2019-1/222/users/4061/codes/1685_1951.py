x0 = float(input("digite x0: "))
y0 = float(input("digite y0: "))
x1 = float(input("digite x1: "))
y1 = float(input("digite y1: "))
x2 = float(input("digite x2: "))
y2 = float(input("digite y2: "))

C = (((x1 - x0)*(y2 - y0))-((x2 - x0)*(y1 - y0)))

if(C < 0):
	mensagem = "A direita da reta"
elif(C > 0):
	mensagem = "A esquerda da reta"
elif(C == 0):
	mensagem = "Sobre a reta"
	
print(mensagem)