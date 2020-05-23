senha = int(input())

a=senha//100000#5
b=(senha//10000)%10#4
c=(senha//1000)%10#3
d=(senha//100)%10#2
e=(senha//10)%10
f=senha%10
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
x=(b+d+f)%(a+c+e)
if (x==0):
	print("acesso liberado")
else:
	print("senha invalida")


