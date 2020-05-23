x= float(input())
k= 5000+(100*x)
v= 28000+(90*(x-200))

if(x == 200) or (x<200):
	msg= k
else:
	msg= v

print(round(msg, 2))