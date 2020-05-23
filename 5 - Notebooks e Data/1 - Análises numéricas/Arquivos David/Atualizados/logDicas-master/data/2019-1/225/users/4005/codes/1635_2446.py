s = int(input())
w= (s//100000)%10
a=(s//10000)%10
b=(s//1000)%10
c=(s//100)%10
d=(s//10)%10
e=(s%10)
f= (a+c+e)%(w+b+d)
if(f==0):
	print("acesso liberado")
else:
	print("senha invalida")