qi = int(input("escreva: "))
pc = int(input("escreva: "))
qv = int(input("escreva: "))

ano=0
cap=12000

while(qi<cap)and(qi>0):
	qi=qi+(qi*(pc/100))-qv
	ano=ano+1
if(qi<0):
	print("EXTINCAO")
if(qi>cap):
	print("LIMITE")
	
print(ano)