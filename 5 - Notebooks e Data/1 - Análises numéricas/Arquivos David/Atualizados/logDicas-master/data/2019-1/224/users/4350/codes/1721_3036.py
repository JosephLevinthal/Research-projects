x = float(input("numero"))
if x<=-1 or x>=1:
	t = x
elif x>-1 and x<0 or x>0 and x<1:
	t = 1
elif x == 0:
	t = 2
print(round(t, 2))