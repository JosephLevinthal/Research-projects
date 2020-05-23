x=int(input("quantidade:"))
for i in range(x,0,-1):
	s=i*"*"+2*(x-i)*"o"+i*"*"
	print(s)