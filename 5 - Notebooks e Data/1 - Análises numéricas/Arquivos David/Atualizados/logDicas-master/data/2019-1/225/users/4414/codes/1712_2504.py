qv= int(input("virus:"))
ql= int(input("leucitos:"))
pv= float(input("p virus:"))
pl= float(input("p leucitos:"))

cqv=qv
cql=ql
c=0

while(cqv*2>cql):
	cql=cql+((cql*pl)/100)
	cqv=cqv+((cqv*pv)/100)
	
	c = c +1

	
print(c)
