n=int(input('senha: '))
a=n // 100000
b=(n // 10000) % 10
c=(n // 1000) % 10
d=(n // 100) % 10
e=(n // 10) % 10
f= n % 10
s= (b +  d + f)
r= (a + c + e)
t= s//r
if(t * r == s):
	print('acesso liberado')
if(t * r != s):
	print('senha invalida')