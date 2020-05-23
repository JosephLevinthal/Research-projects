t=input()

t1=t.upper()
t1=t1.replace("","")
print(t1)

t2=""
i=0
while(i<len(t1)):
	t2=t2+t1[-1-i]
	i=i+1
if(t2==t1):
	print(1)
else:
	print(0)