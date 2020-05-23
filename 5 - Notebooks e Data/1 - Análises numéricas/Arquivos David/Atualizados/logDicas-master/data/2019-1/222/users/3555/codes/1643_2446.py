from math import*
s = int(input())

q = str(s)
q = len(q)

n1 = s//100000
s = s - n1*100000
n2 = s // 10000
s = s - n2*10000
n3 = s // 1000
s = s - n3*1000
n4 = s // 100
s = s - n4*100
n5 = s // 10
s = s - n5*10
n6 = s // 1
s = s - n6*1
#print(n1,n2,n3,n4,n5,n6)

x = (n2+n4+n6)
y = (n1+n3+n5)

#print(x,y)

if(x%y == 0):
	print("acesso liberado")
else:
	print("senha invalida")

