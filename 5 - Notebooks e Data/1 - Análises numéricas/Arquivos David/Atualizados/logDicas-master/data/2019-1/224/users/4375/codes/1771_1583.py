from numpy import*
number=input("write number: ")
cop=""
i=0
while(i<len(number)):
	if((i+1)%3 == 0 and i<(len(number)-1)):
		cop=cop + str(number[i])+"."
	else:
		cop=cop + str(number[i])
	i=i+1
print(cop)