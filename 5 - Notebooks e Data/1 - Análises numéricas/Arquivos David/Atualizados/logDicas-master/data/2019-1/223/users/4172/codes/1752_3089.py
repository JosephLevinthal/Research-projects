m=int(input("movimento em metros: "))

soma=0


while(m!=0):
	soma+=m
	m=int(input("movimento em metros: "))
print(soma)
	
if(soma>0):
	print("Direita")
if(soma<0):
	print("Esquerda")
if(soma==0):
	print("Inicial")