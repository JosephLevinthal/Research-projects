x=int(input("Digite uma senha :"))
a=x//100000
b=(x//10000)%10
c=(x//1000)%10
d=(x//100)%10
e=(x//10)%10
f=x%10
g=(b+d+f)%(a+c+e)
if(g == 0):
	print("acesso liberado")
else:
	print("senha invalida")