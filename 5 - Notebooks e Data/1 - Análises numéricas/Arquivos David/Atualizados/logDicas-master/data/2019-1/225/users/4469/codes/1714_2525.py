x = int(input())

c = 1
qd = 0

while(c <= x):
	if(x % c == 0):
		print(c)
		qd = qd + 1
	
	c = c + 1

print(qd, "divisores")