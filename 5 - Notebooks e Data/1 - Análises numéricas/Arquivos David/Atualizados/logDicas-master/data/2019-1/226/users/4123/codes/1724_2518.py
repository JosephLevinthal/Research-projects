n = int(input())
if n<1:
	n = 1
while n!=1:
	if n%2==0:
		n = n/2
	else:
		n = n*3 + 1
	print(int(n))