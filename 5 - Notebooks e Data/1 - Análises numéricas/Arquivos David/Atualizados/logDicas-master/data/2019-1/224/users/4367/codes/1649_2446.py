s= int(input("digite uma senha de 6 digitos:"))
n1=s//100000
n2=s%100000//10000
n3=s%100000%10000//1000
n4=s%100000%10000%1000//100
n5=s%100000%10000%1000%100//10
n6=s%100000%10000%1000%100%10
c= n2+n4+n6
v= n1+n3+n5
if(c%v)==0:
	print("acesso liberado")
else:
	print("senha invalida")