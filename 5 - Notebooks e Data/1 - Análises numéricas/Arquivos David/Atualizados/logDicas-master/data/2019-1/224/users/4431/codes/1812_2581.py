from numpy import*
x=array(eval(input("Digite as entradas: ")))
t=0
r=0
y=0
u=0
while(size(x)>1):
	t=t+x[1]
	r=r+x[2]
	y=y+x[3]
	u=u+x[4]
	x=array(eval(input("Digite as entradas: ")))
print("ADM")
print("Entrada: ",t)
print("Saida: ",r)
print("CHAO")
print("Entrada: ",y)
print("Saida: ",u)