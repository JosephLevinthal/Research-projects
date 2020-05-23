senha=int(input())

a=senha//100000
b=(senha - a*100000)//10000
c=(senha - a*100000 - b*10000)//1000
d=(senha - a*100000 - b*10000 - c*1000)//100
e=(senha - a*100000 - b*10000 - c*1000 - d*100)//10
f=(senha - a*100000 - b*10000 - c*1000 - d*100 - e*10)

if ((b+d+f)%(a+c+e)==0):
	print("acesso liberado")
else:
	print("senha invalida")