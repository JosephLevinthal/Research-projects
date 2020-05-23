from numpy import*
p=array(eval(input("****: ")))
for i in range (p):
	print("*" * (p-i) + "o" * i + "o" * i + "*" * (p-i))
