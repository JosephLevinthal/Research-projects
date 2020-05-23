ano=0
ca=int(input("habitantes de a: "))
cb=int(input("habitantes de b: "))
tca=float(input("taxa de crescimento de A: "))
tcb=float(input("taxa de crescimento de B: "))
while(ca<=cb):
	ca+=(ca*(tca/100))
	cb+=(cb*(tcb/100))
	ano+=1
print(ano)
