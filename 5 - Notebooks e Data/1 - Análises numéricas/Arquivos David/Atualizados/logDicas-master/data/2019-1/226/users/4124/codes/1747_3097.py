soma = 0
pt = 0
pos = int(input("Posicao do joquei: "))
while(pos != 0):
	#pos = int(input("Posicao do joquei: "))
	if(pos == 1):
		pt = 25
	elif(pos == 2):
		pt = 18
	elif(pos == 3):
		pt = 12
	elif(pos >= 4 and pos <= 10):
		pt = 14 - pos
	elif(pos < 0 or pos > 10):
		pt = 0
	pos = int(input("Posicao do joquei: "))
	soma = soma + pt
print(soma)
	