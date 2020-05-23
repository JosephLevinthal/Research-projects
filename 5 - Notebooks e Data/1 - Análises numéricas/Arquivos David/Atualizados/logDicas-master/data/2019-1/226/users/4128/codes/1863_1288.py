from numpy import*	
from numpy.linalg import*

a = array(eval(input("entrada:")))

tt = [[5, 10, 10, 100]]
bnb = [[6, 10, 100, 30]]
be = [[5, 50, 20, 20]]
cdv = [[15, 20, 40, 35]]

preco = [[5,6,5,15]]
nitrato = [[10,10,50,20]]
fosfato = [[10,100,20,40]]
potassio = [[100,30,20,35]]

for x in range(size(a)):
	b = a - tt
	c = a - bnb
	d = a - be
	e = a - cdv
	f = a[0] - preco
print("titica:",b )
print("barro no balde:",c )
print("bestrume:",d )
print("caca de vaca",e )
print(f)
