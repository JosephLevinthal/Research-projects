qi = int(input("escreva: "))
ql = int(input("escreva: "))
pv = int(input("escreva: "))
pl = int(input("escreva: "))

dia=0

while(ql<=2*qi):
	qi=qi+(qi*(pv/100))
	ql=ql+(ql*(pl/100))
	dia=dia+1
	
print(dia)