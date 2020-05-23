from numpy import *
num = input("d")
copy = ""
i = 0
while(i<len(num)):
	if((i+1)%3 == 0 and i<(len(num)-1)):
		copy = copy + str(num[i]) + "."
	else:
		copy = copy + str(num[i])
	i = i + 1
print(copy)