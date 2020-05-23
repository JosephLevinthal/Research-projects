n=int(input("senha: "))
x1= n // 100000
x2=n%100000//10000
x3=n%10000//1000
x4=n%1000//100
x5=n%100//10
x6=n%10
if((x2+x4+x6) % (x1+x3+x5) == 0):
	print("acesso liberado")
else:
	print("senha invalida")
