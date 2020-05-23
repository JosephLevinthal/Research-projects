h=float(input())
s=input()

ph=72.7*h - 58
pm=62.1*h - 44.7

if (s=='M'):
	print(round(ph,2))
else:
	print(round(pm,2))