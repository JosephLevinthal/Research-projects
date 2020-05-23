qi=int(input("quantidade inicial: "))
pc=float(input("percentual de crescimento: "))

m=0
y=0
while(0<qi and 8000>qi):
	qi=qi+(qi*(pc/100))
	r=int(input("retirada por mes: "))
	qi-=r
	m+=1
if(qi<0):
	print("ZERO")
else:
	print("MAXIMO")
print(m)	