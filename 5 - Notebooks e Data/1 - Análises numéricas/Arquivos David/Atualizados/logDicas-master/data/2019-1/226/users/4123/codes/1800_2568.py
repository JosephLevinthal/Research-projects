n = int(input())
i = 0
j = ""
for i in range(0,n):
	j+=(n-i)*"*"
	j+=2*i*"o"
	j+=(n-i)*"*"
	print(j)
	j=""
	