q=int(input("Quantidade inicial: "))
p=int(input("percentual de crescimento: "))

t=0
while(q<8000 and q>0):
	r=int(input("qtd retirada todos os anos: "))
	h=(q*p)/100
	q=q+h-r
	t+=1
if(q>=8000):
	print("MAXIMO")
elif(q<=0):
	print("ZERO")
print(t)