x = 1
sp = 0
si = 0
cp = 0
ci = 0

while(x != 0):
	x = int(input())
	
	if(x == 0):
		break
	
	if(x % 2 == 0):
		sp = sp + x
		cp = cp + 1
	else:
		si = si + x
		ci = ci + 1


if(cp == 0 and ci != 0):
	mi = si/ci
	print(0.0)
	print(round(mi, 2))
elif(cp != 0 and ci == 0):
	mp = sp/cp
	print(round(mp, 2))
	print(0.0)
else:
	mi = si/ci
	mp = sp/cp
	print(round(mp, 2))
	print(round(mi, 2))