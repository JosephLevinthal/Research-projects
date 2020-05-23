q = input()
t = float(input())

if(q=="F"):
	c = 5/9 * (t - 32)
	print(round(c,2))
else:
	f =  (t * 1.8) + 32 
	print(round(f,2))