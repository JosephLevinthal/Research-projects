qp = int(input("escreva: "))
pc = int(input("escreva: "))
qr = int(input("escreva: "))

mes=0
cap=8000

while(qp>0)and(qp<cap):
	qp=qp+(qp*(pc/100))-qr
	mes=mes+1
	if(qp>=cap):
		print("MAXIMO")
	elif(qp<=0):
		print("ZERO")
	else:
		qr = int(input("escreva: "))
		
print(mes)