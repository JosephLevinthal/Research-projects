from numpy import*
a = array(eval(input("A: ")))
b = array(eval(input("b: ")))
i = 0

while(i < size(a)):
	b[-i] = a[i]
	i = i + 1
print(a)
print(b)


	
	