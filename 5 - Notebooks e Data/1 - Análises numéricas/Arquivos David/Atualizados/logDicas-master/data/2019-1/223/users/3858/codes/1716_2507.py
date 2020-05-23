qi = int(input())
pc = float(input())/100

c = 0
while(qi>0 and qi<8000):
	qi = qi + (qi*pc)
	qr = int(input())
	if(qi>=0 and qi<=8000):
		qi = qi - qr
		mensagem = "ZERO"
	else:
		mensagem = "MAXIMO"
	c = c +1
print(mensagem)
print(c)