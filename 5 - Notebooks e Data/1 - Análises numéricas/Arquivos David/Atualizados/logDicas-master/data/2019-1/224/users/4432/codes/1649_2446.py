senha=float(input("digite uma senha:      "))
x=senha//100000    #primeiro numero
y=(senha//10000)%10   #segundo numero
z=(senha//1000)%10    #terceiro numero
a=(senha//100)%10     #quarto numero
b=(senha//10)%10     #quinto numero
c=senha%10           #sexto numero
if((y+a+c)%(x+z+b)!=0):
	print("senha invalida")
else:
	print("acesso liberado")
	