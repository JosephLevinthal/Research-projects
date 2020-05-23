a = int(input("thanos:"))
k = 1
i = 0 

while(i < a):
	a = a // k
	i = i + 1
	k = k + 1 
	
	print(a)
if(k == a):
	print("1 divisor")
else:
	print(i,"divisores")