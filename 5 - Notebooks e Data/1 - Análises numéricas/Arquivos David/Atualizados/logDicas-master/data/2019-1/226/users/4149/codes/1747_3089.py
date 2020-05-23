mov=int(input("entre com o movimento:"))
soma=0
while(mov!=0):
	mov=int(input("entre com o movimento:"))
	soma=soma+mov
	
print(soma)	
if(soma<0):
	print("Esquerda")
		
elif(soma==0):
	(print("inicial"))
elif(soma>0):
	print("Direita")
	
	