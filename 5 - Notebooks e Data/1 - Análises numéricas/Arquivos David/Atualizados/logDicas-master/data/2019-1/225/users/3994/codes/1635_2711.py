d = float(input())
t = int(input())
vt = float(input())
p = int(input())
vp = float(input())
A = (t * vt + p * vp)
if(d > A):
	msg = " SUFICIENTE "
else:
	msg = " INSUFICIENTE "
	
print(msg)