from numpy import*

a = array(eval(input("Digite os valores: ")))

i = 0
p = 0
b = 0
while(i < size(a)):
	if(a[i] > 99):
		i = i
		b = b + 1
		print(i)
	else:
		b = b + 0
	i = i + 1

print(b)	
		