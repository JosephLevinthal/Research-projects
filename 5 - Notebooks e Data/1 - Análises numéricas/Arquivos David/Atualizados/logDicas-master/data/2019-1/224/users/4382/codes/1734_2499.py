from math import factorial
k = int(input("termos : "))
e = 0 
i = 0
while(i < k):
	e = e + 1/factorial(i)
	i = i + 1
print(round(e , 8))
