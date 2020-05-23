x = int(input("movimento"))

soma = 0

while(x!=0):
	soma = soma + x
	
	x = int(input("movimento"))
	
print(soma)

if(soma<0):
	print("Abaixo")
elif(soma>0):
	print("Acima")
else:
	print("Inicial")
	
