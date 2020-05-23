h = float(input())
s = float(input())
d = float(input())

t = 0
p = 0

while(p != h):
	if(p < h):
		p = p + s - d
	elif(p > h):
		p = p - s + d
		
	t = t + 1
	
print(t)