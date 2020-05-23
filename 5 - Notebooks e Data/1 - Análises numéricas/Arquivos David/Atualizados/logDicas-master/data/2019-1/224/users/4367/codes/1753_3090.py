x=int(input("digite o numero de passos da largatixa: "))
c=0
d=x
while(x!=0):
	x=int(input("digite o numero de passos da largatixa: "))
	d=d+x
if(d>0):
	print(d)
	print("Acima")
elif(d<0):
	print(d)
	print("Abaixo")
elif(d==0):
	print(d)
	print("Inicial")