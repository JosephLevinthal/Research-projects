m = int(input("Movimento: "))

a = 0


while(m != 0):
	p = m + a
	a = p
	
	m = int(input("Movimento: "))
	
print(p)
	
if(p > 0):
	print("Direita")
elif(p < 0):
	print("Esquerda")
elif(p == 0):
	print("Inicial")