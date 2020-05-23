from numpy import*
mt=array(eval(input("numeros de matriculas: ")))
d=0
for i in range (size(mt)):
	if(mt[i]%2!=0):
		d=d+1
c=zeros(d, dtype=int)
v=0
for i in range (size(mt)):
	if(mt[i]%2!=0):
		c[v]=c[v]+mt[i]
		v=v+1
print(c)
	