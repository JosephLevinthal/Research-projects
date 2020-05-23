senha=int(input("senha :"))
n1=senha//100000
r1=senha % 100000
n2=r1 // 10000
r2= r1% 10000
n3=r2 // 1000
r3= r2 % 1000
n4= r3 // 100
r4= r3 % 100
n5= r4 // 10
r5= r4 % 10
n6= r5 // 1
r6= r5 % 1

m=(n2 + n4 + n6) % (n1 + n3 + n5) 

if (m == 0) :
	print("acesso liberado")	
else :
	print("senha invalida")