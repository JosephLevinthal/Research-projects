n= int(input("qual seu termo geral?"))
pi=0
i=0

while(i<n):
	pi=pi + (4/(2*i+1))*(-1)**i
	i=i+1
print(round(pi,8))
	