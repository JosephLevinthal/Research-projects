from numpy import*
n = int(input("Numero inteiro positivo e maior do que 2: "))

v = array([n])

i = 0
fim = n - 1
f = 0

d = zeros(n,dtype=int)
d[0]=0
d[1]=1
d[i]=0

while(i < size(d)):
	i = i + 1
	f = f + 1
print(d)

