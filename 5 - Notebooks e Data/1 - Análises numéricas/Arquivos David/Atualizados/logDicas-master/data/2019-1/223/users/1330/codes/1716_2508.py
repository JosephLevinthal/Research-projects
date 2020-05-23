n = int(input())

soma = 3
i = 1

while(i<n):
	x = (2*i)*(2*i+1)*(2*i+2)
	soma = soma + (-1)**(i+1)*4/x
	i = i +1
	
print(round(x,8))