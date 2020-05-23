n = int(input())-1
pi = 3
i = 0

while i<n:
	pi+= 4/((2+2*i)*(3+2*i)*(4+2*i))*(-1)**i
	i+=1
print(round(pi,8))