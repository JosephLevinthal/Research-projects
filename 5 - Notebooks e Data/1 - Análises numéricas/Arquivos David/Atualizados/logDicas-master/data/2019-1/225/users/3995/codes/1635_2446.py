s=int(input("senha:"))
x=s//100000
y=(s//10000)%10
w=(s//1000)%10
z=(s//100)%10
u=(s//10)%10
v=s%10
h=(y+z+v)%(x+w+u)
if(h==0):
	msg=("acesso liberado")
else:
	msg=("senha invalida")
print(msg)