copias = int(input("digite copias: "))
leucocitos = int(input("digite leucocitos: "))
pervirus = int(input("digite percentual virus: "))
perleuco = int(input("digite percentual leuco: "))

quantV = 1
quantL = 0
cont = 1
leu = 0

while(leu != 10):
	quantL = ((perleuco/100)*leucocitos)+leucocitos
	quantV = ((pervirus/100)*copias)+copias
	cont = cont + 1
	if(quantL*2 > quantV):
		leu = 10
	
	
print(cont)
	
	
	
