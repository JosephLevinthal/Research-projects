e = input("C,F:")
temp = float(input("t:"))

if(e=="C"):
	print(round(9/5*temp+32,2))
else:
	print(round(5/9*(temp-32),2))