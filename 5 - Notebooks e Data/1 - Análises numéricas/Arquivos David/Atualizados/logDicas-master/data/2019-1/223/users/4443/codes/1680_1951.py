#Leitura das coordenadas dos pontos
x0 = float(input("Digite o valor de x para o ponto 0: "))
y0 = float(input("Digite o valor de y para o ponto 0: "))
x1 = float(input("Digite o valor de x para o ponto 1: "))
y1 = float(input("Digite o valor de y para o ponto 1: "))
x2 = float(input("Digite o valor de x para o ponto 2: "))
y2 = float(input("Digite o valor de y para o ponto 2: "))

c = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0)
if(c < 0):
	print("A direita da reta")
elif(c > 0):
	print("A esquerda da reta")
elif(c == 0):
	print("Sobre a reta")