from numpy import*
c1=int(input("insira a cidade 1: "))
c2=int(input("insira a cidade 2: "))
mt=array([[0,2,11,6,15,11,1],
[2,0,7,12,4,2,15],
[11,7,0,11,8,3,13],
[6,12,11,0,10,2,1],
[15,4,8,10,0,5,13],
[11,2,3,2,5,0,14],
[1,15,13,1,13,14,0]])
if (c1==111):
	i=0
elif (c1==222):
	i=1
elif (c1==333):
	i=2
elif (c1==444):
	i=3
elif (c1==555):
	i=4
elif (c1==666):
	i=5
elif (c1==777):
	i=6
if (c2==111):
	j=0
elif (c2==222):
	j=1
elif (c2==333):
	j=2
elif (c2==444):
	j=3
elif (c2==555):
	j=4
elif (c2==666):
	j=5
elif (c2==777):
	j=6
s=(mt[i,j])
c=int(input("insira a proxima cidade: "))

while c != -1:
	if (c2==111):
		i=0
	elif (c2==222):
		i=1
	elif (c2==333):
		i=2
	elif (c2==444):
		i=3
	elif (c2==555):
		i=4
	elif (c2==666):
		i=5
	elif (c2==777):
		i=6
	if (c==111):
		j=0
	elif (c==222):
		j=1
	elif (c==333):
		j=2
	elif (c==444):
		j=3
	elif (c==555):
		j=4
	elif (c==666):
		j=5
	elif (c==777):
		j=6
	s=s+mt[i,j]
	c2=c
	c=int(input("insira a proxima cidade: "))
print(s)