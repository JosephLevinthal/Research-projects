a = senha// 1000000
b=(senha//100000)%10
c=(senha//1000)%10
d=(senha//100)%10
e(senha//10)%10
f=senha%10

x=(b+d+f)%(a+c+e)
if(x==0):
	print("acesso liberado")
else:
	print("senha invalida")