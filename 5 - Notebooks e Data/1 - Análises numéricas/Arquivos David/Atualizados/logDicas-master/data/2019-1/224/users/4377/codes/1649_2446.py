nu=int(input("numero"))
n1=nu//100000
r=nu%100000
n2=r//10000
r=r%10000
n3=r//1000
r=r%1000
n4=r//100
r=r%100
n5=r//10
n6=nu%10
if ( (n1+n3)%(n2+n4)%(n5+n6) != 0 )  :
	print("acesso liberado")
else :
	print("senha invalida")