from numpy import*

j = array(eval(input('')))
b=0

for i in j:
	if(i%2!=0):
	  	b= b + 1
p = zeros(b, dtype=int)
x=0
g=0

for t in j:
	if(t%2!=0):
		p[x]=j[g]
		x = x + 1
	g = g + 1
print(p)



		