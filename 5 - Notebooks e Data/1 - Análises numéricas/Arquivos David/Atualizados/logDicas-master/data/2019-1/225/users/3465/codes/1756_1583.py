string = input("")
string2 =''
i = 3
j = 0
print(string.upper())
while(i<len(string)):
	string2+=string[j:i]+"."
	j = i
	i+=3
string2+=string[j::]
print(string2)