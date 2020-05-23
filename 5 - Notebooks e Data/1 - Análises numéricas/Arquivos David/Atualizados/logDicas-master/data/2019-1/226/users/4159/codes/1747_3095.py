res = input("resultado do jogo: V/E/D (para fechar X)").upper()
v = 0
e = 0
d = 0
while(res!="X"):
	if(res=="V"):
		v = v + 3
	elif(res=="E"):
		e = e + 2
	elif(res=="D"):
		d = d + 1
	res = input("novo resultado ").upper()
print(v)
print(e)
print(d)
		