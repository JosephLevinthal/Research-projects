s1=int(input("senha 1: "))
w = (s1//100000)%10
x = (s1//10000)%10
y = (s1//1000)%10
z = (s1//100)%10
a = (s1//10)%10
b = s1%10
j=x+z+b
h=w+y+a
k=j%h
if(k==0):
	msg="acesso liberado"
else:
	msg="senha invalida"
print(msg)