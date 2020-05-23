vv = float(input())

if(vv <= 1000):
	print(round(0.05*vv,2))
else:
	a = 0.05*1000 + 0.1*(vv-1000) 
	print(round(a,2))