p = int(input("posicao de chegada:"))

acum = 0
cont = 0

while(p != 0 ):
	if(p == 1):
		acum = acum + 25
	elif(p == 2):
		acum = acum + 18
	elif(p == 3):
		acum = acum + 12
	elif(p>=4 and p <= 10):
		acum = acum + (14 - p)
	else:
		acum = acum + 0
	cont = cont + 1
	
	p = int(input("posicao de chegada:"))
print(acum)