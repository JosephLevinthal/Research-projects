a=int(input("habitantes de A: "))
b=int(input("habitantes de B: "))
pa=float(input("percentual A: "))
pb=float(input("percentual B: "))
t=0
while(a<b):
	a=a+a*(pa/100)
	b=b+b*(pb/100)
	t = t+1
print(t)