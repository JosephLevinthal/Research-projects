n = int(input("digite um numero: "))
d = 0
while(n!=0):
	d= d+n
	n=int(input("digite um numero: "))


print(d)
if(d<0):
	print("Esquerda")
elif(d==0):
	print("Inicial")
else:
	print("Direita")