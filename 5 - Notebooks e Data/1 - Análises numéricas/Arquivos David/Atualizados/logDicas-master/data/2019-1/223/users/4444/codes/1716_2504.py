v=int(input("quantidade de virus: "))
l=int(input("qtd leucocitos: "))
pv=float(input(" percentual de mut virus: "))
pl=float(input(" percentual de mut leococutos: "))

dias=0
i=0
while(l<=2*v):
	v=v+v*pv/100
	l=l+l*pl/100
	i=i+1
	dias=dias+1
print(dias)
	