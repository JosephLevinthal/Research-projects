a = int(input("no. hab cid: "))
b = int(input("no. hab cid: "))
pa = float(input("percentual da cid: "))
pb= float(input("percentual da cid: "))
ano = 0
while(b>=a):
	cresca = (a*pa)/100
	crescb = (b*pb)/100
	a= a + cresca
	b= b + crescb
	ano = ano + 1
print(ano)